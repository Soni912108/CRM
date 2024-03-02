from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Define your app's URL patterns here
    path('logout_view/',views.logout_view,name='logout_view'),
    path('profile_view/',views.profile_view,name='profile_view'),
    
]