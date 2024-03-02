from . import views
from django.urls import path

app_name = 'crm'

# all of the paths have crm/ before them. example crm/cars to show all the cars and their data 
urlpatterns = [ 
    # Define your app's URL patterns here
    path('dashboard/', views.dashboard, name='dashboard'),
    # customers
    path('customer/', views.customer_details, name='customer_details'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<int:user_id>/', views.update_customer, name="update_customer"),
    path('delete_customer/<int:user_id>/', views.delete_customer, name='delete_customer'),
    # cars get_car_options
    path('cars/', views.show_all_cars, name='show_all_cars'),
    path('add_car/', views.add_car, name='add_car'),
    path('get_car_details/', views.get_car_details, name='get_car_details'),
    path('update_car/<int:car_id>/', views.update_car, name='update_car'),
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),
    # sell
    path('transaction_list/', views.transaction_list, name='transaction_list'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('update_transaction/<int:transaction_id>/', views.update_transaction, name='update_transaction'),
    path('delete_transaction/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('sold/', views.sold, name='sold'),
    # lease
    path('leasing_list/', views.leasing_list, name='leasing_list'),
    path('add_lease/', views.add_lease, name='add_lease'),
    path('update_lease/<int:lease_id>/', views.update_lease, name='update_lease'),
    path('delete_lease/<int:lease_id>/', views.delete_lease, name='delete_lease'),
    path('lease/', views.lease, name='lease'),
    
]