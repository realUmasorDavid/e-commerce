from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail', views.detail, name='detail'),
    path('order', views.order, name='order'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup, name='register'),
    path('logout', views.logout, name='logout'),
]