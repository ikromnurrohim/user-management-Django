from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
	path('accounts/', include('account.urls', namespace='accounts')),
	path('', views.index, name='home'),
    path('admin/', admin.site.urls),
]
