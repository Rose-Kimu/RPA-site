from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate,login,logout

# def index(request):
#     reports = Report.objects.all()
#     context = {'reports':reports}

#     return render(request, 'myapp/report-list.html', context)

def createReport(request):
    form = ReportForm()

    if request.method == 'POST':
        print('Printing post', request.POST)
        form = ReportForm(request.POST)
        print('form object created')
        if form.is_valid():
            print('Valid form')
            form.save()
            print('Form saved')
            return redirect('view_all_reports')
        else:
            print('Form errors:', form.errors)
    
    context = {
        'form':form
        
    }
    print('Rendering the form')
    return render(request, 'myapp/example.html', context)

def addReportBtn(request):
    return render(request, 'myapp/add-report-btn.html')

def viewAllReports(request):
    reports = Report.objects.all()
    context = {'reports':reports}
    return render(request, 'myapp/report-list.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password  = request.POST.get('password')

        user = authenticate(request, username=username, password= password)

        if user is not None:
            login(request, user)
            print('logged in')
            return redirect('add_report_btn')
        

    return render(request, 'myapp/login-old.html')

def registerUser(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse("<h1> Registration succesful </h1>")
    else :
        user_form = UserCreationForm()
    # user_form = UserCreationForm()

    context = {
        'user_form': user_form
    }

    return render(request, 'myapp/register.html', context)
