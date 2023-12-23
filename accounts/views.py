from django.shortcuts import render, redirect
from . models import *
from .forms import *
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group

# Create your views here.
@login_required(login_url='accounts:login')
@admin_only
def home(request):
    customers=Customer.objects.all()
    orders = Order.objects.all()
    total_customers=customers.count()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    context ={
        'customers':customers,
        'orders':orders,
        'total_customers':total_customers,
        'total_orders':total_orders,
        'delivered':delivered,
        'pending':pending
    }

    return render(request,'accounts/dashboard.html',context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all() 
    # context=products
    return render(request, 'accounts/products.html',{'products':products})


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk_test): 
    customer=Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    total_orders=orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders=myFilter.qs
    context={
        'customer':customer,
        'orders':orders,
        'total_orders':total_orders,
        'myFilter':myFilter
    }
    return render( request, 'accounts/customer.html',context)


def createOrder(request,pk):
    customer = Customer.objects.get(id=pk)
    print(customer)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.customer=customer
            order.save()

            return redirect('accounts:home')
    else:
        form = OrderForm()
        context={
        'form': form,

                    }
        return render(request,'accounts/order_form.html',context)
    

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form': form}
	return render(request, 'accounts/order_form.html', context)

def deleteOrder(request,pk) :
     order = Order.objects.get(id=pk)
     if request.method == 'POST':
          order.delete()
          return redirect('accounts:home')
     context={'item':order}
     return render(request,"accounts/delete.html", context)


@unauthorized_users
def sign_up(request):
  
   form = CreateUserForm()
   if request.method == 'POST':

     form = CreateUserForm( request.POST)
     if form.is_valid():
          user=form.save()
          group = Group.objects.get(name='customer')
          user.groups.add(group)

          user=form.cleaned_data.get('username')
          messages.success(request,'account  created'+ user)
          return redirect('accounts:login')
     


  
        
   
   context={
         'form':form
              }
   return render(request,'accounts/sign_up.html',context)


@unauthorized_users
def login_view(request):

    if request.method == 'POST':
          
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a success page.
            return redirect('accounts:home') 
        else:
             messages.info(request, 'password or username incorrect')
    
    form = AuthenticationForm()
    context= {
          'form':form
            }
    return render(request,'accounts/login.html',context)


def logout_view(request):
     
          logout(request)
          return redirect('accounts:login')
     


def userPage(request):
     context={}

     return render(request,'accounts/user.html', context)