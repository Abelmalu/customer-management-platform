from django.shortcuts import render, redirect
from . models import *
from .forms import OrderForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout


# Create your views here.

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


def products(request):
    products = Product.objects.all() 
    # context=products
    return render(request, 'accounts/products.html',{'products':products})

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


def sign_up(request):
   if request.method == 'POST':

     form = UserCreationForm(request,request.POST)
     if form.is_valid():
          form.save()
          return redirect('accounts:home')


   else:
        form = UserCreationForm()
        context={
         'form':form
          }
        return render(request,'accounts/sign_up.html',context)






def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a success page.
            return redirect('accounts:home') 
    else:
       form = AuthenticationForm()
       context= {
          'form':form
            }
       return render(request,'accounts/login.html',context)


