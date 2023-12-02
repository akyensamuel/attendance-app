from django.shortcuts import render, redirect
from django.forms.models import modelform_factory
from .models import Absentee
from datetime import datetime, timedelta 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request, 'index.html', {})

@login_required(login_url='admin-login')
def admin(request):
    AbsenteeForm = modelform_factory(model=Absentee, fields='__all__')
    if request.method == 'GET':
        form = AbsenteeForm()
    else: 
        form = AbsenteeForm(request.POST)
        if form.is_valid():
            form.save()
            form = AbsenteeForm()
    return render(request, 'admin-page.html', {'form':form})

def test(request):
    dateToday = datetime.today().date()
    dateYesterday = dateToday + timedelta(days=-1)
    absenteesToday = Absentee.objects.filter(date=dateToday)
    absenteesYesterday = Absentee.objects.filter(date=dateYesterday)
    days = [{'label':'Yesterday', 'list': absenteesYesterday}, {'label':'Today', 'list': absenteesToday}]
    return render(request, 'table.html', {'days': days})

def adminLogin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else: 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_superuser:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('admin-page')
        else: 
            messages.error(request, 'Access Denied')
            return render(request, 'login.html', {})
        
def adminLogout(request):
    logout(request)
    return redirect('admin-login')
    
# how to check if a user is a super user in django ?