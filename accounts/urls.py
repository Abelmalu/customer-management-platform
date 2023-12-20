from django.urls import path
from . import views


app_name='accounts'

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('customer/<str:pk_test>',views.customer, name='customer'),
    path('create_order/<str:pk>', views.createOrder, name='create_order'),
    path('update_order/<str:pk>', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>', views.deleteOrder, name='delete_order'),
    path('login/', views.login_view, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout_view/', views.logout_view, name='logout'),
]