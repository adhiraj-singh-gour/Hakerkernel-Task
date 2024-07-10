from django.shortcuts import render,redirect
from .forms import UserForm,TaskForm
from .models import *
from django.core.paginator import Paginator
from django.http import HttpResponse
import openpyxl
from openpyxl import Workbook

def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(UserList) 
    else:
        form = UserForm()
    return render(request,'user.html', {'form': form})

def UserList(request):
    users = User.objects.all()
    paginator = Paginator(users, 10) 
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'UserList.html', {'page': page})


def tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(TaskList) 
    else:
        form = TaskForm()
    return render(request, 'task.html', {'form': form})

def TaskList(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 10) 
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'TaskList.html', {'page': page})


def Task_into_excell(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Data"
    headers = ['Task Details', 'Task Type', 'User']
    ws.append(headers)
    tasks = Task.objects.all()
    for task in tasks:
        task_details = task.task_details
        task_type = task.task_type 
        user_name = task.User.name 
        row = [task_details, task_type, user_name]
        ws.append(row)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=data.xlsx'
    wb.save(response)
    return response

def User_to_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Data"
    headers = ['Name', 'Email', 'Mobile','ID'] 
    ws.append(headers)
    data = User.objects.all().values_list('name', 'email', 'mobile','ID') 
    for row in data:
        ws.append(row)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=data.xlsx'
    wb.save(response)
    return response

