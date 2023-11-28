from django.shortcuts import render, redirect
from django.forms.models import modelform_factory
from .models import Absentee
from datetime import datetime, timedelta 

def index(request):
    return render(request, 'index.html', {})

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