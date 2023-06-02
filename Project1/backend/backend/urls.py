"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('search_flights/', user_views.search_flights, name='search_flights'),
    path('book_flight/<int:flight_id>/', user_views.book_flight, name='book_flight'),
    path('my_bookings/', user_views.my_bookings, name='my_bookings'),
    path('add_flight/', user_views.add_flight, name='add_flight'),
    path('show_flights/', user_views.show_flights, name='show_flights'),
    path('show_flights_user/', user_views.show_flights_user, name='show_flights_user'),
    path('remove_flight/', user_views.remove_flight, name='remove_flight'),
    path('view_bookings/', user_views.view_bookings, name='view_bookings'),
    path('cancel_flight/', user_views.cancel_flight, name='cancel_flight'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

