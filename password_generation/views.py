from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'password_generation/home.html')


def password(request):
    characters = list('abcdefjhijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+<>?":'))
    length = int(request.GET.get('length', 12))
    print(length, 'qwerty')
    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)

        print(the_password)
    return render(request, 'password_generation/password.html', {'password': the_password})
