from django.shortcuts import render
from django.http import HttpResponse
import random
from django.shortcuts import render
from .forms import UserInputForm
from django.core.mail import send_mail
from .models import UserGeneratedPassword
from django.db import connection
import os


def home(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT count(*) FROM password_generation_usergeneratedpassword''')
    row = cursor.fetchone()[0]
    row1 = f'На нашем сайте уже было сгенерировано {row} паролей!'
    return render(request, 'password_generation/home.html', {'quantity': row1})


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
        print("passw", the_password)
        return render(request, 'password_generation/home.html', {'error': 'Please input name and email'})
    print("render partially")
    return render(request, 'password_generation/password.html', {'password': the_password})


def save_generated_password(name, email, the_password):
    print(name, email, the_password)
    UserGeneratedPassword.objects.create(name=name, email=email, generated_password=the_password)


def context(request):
    some_information = 'some_information.txt'
    file_path = os.path.join(os.path.dirname(__file__), some_information)
    with open(file_path, 'r') as file:
        file_content = file.read()

    return render(request, 'password_generation/context.html', {'some_information': file_content})


def support(request):
    support_information = 'support.txt'
    file_path = os.path.join(os.path.dirname(__file__), support_information)
    with open(file_path, 'r') as file:
        file_content = file.read()

    return render(request, 'password_generation/support.html', {'support_information': file_content})
