from django.urls import path 
from . import views 
urlpatterns = [
    path('', views.test, name='index'),
    path('admin-page/', views.admin, name='admin-page'),
    path('admin-login/', views.adminLogin, name='admin-login'),
    path('admin-logout/', views.adminLogout, name='admin-logout'),
    path('test/', views.index, name='test'),
]