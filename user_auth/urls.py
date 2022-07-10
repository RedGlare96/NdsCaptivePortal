from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'user_auth'

'''
path('signup/', views.signupuser, name='signupuser'),
path('loginuser/', views.loginuser, name='loginuser'),
'''
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signupuser, name='signupuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('registeruser/', views.register_user, name='reg_user'),
    path('pportal/', views.payment_portal, name='p_portal'),
    path('dlogout/', views.logout_debug, name='debug_logout'),
]