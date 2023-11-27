from django.urls import path 
from . import views 
urlpatterns = [
    path('', views.test, name='index'),
    path('admin-page/', views.admin, name='admin-page'),
    path('test/', views.index, name='test'),
]