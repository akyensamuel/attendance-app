from django.urls import path 
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('admin-page/', views.admin, name='admin-page'),
    path('test/', views.test, name='test'),
]