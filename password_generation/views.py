from django.shortcuts import render
from django.http import HttpResponse
import random
from django.shortcuts import render
from .forms import UserInputForm
from django.core.mail import send_mail
from .models import UserGeneratedPassword


def home(request):
    return render(request, 'password_generation/home.html')


def password(request):
    name = ''
    email = ''
    if request.GET.get('name'):
        name = request.GET.get('name')
    if request.GET.get('email'):
        email = request.GET.get('email')
    characters = list('abcdefjhijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+<>?":'))
    length = int(request.GET.get('length', 12))
    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)
    print(the_password)
    if name and email:
        save_generated_password(name, email, the_password)
    else:
        return render(request, 'password_generation/home.html', {'error': 'Please input name and email'})
    return render(request, 'password_generation/password.html', {'password': the_password})


def save_generated_password(name, email, the_password):
    print(name, email, the_password)
    UserGeneratedPassword.objects.create(name=name, email=email, generated_password=the_password)
