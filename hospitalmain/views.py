from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout



from django.views.decorators.csrf import csrf_exempt

from hospitalhome.models import User


@csrf_exempt
def login_user(request):
    page = 'patient_login'
    if request.method == 'GET':
        return render(request, 'paitent-login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_patient:   
                messages.success(request, 'User Logged in Successfully')    
                return redirect('patient-dashboard')
            else:
                messages.error(request, 'Invalid credentials. Not a Patient')
                return redirect('logout')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'paitent-login.html')

def not_working(request):
    return render(request, 'paitent-login.html')