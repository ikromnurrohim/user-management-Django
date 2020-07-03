from django.urls import path 
from django.contrib.auth.views import LogoutView, LoginView
from .views import *


app_name = 'account'

urlpatterns = [
	path('', account, name='index'),
	path('manage/', list_user, name='list_user'),
	path('logout/', logout_page, name='logout'),
	path('login/', login_page, name='login'),
	path('create_user/', create_user, name='create_user'),
	path('delete_user/<int:pk>/', delete_user, name='delete_user'),
	path('update_user/<int:pk>/', update_user, name='update_user'),
]
