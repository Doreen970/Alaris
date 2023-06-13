from django.urls import path
from . import views

app_name = 'talk'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_talk, name='new'),
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
]