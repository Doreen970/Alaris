from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
from .views import my_logout

app_name = 'duka'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('contact/', views.contact, name = 'contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='duka/login.html', authentication_form=LoginForm), name='login'),
    path('logout/',views.my_logout, name='logout'),
]