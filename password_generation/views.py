from django.shortcuts import render
from django.http import HttpResponse
import random
from django.shortcuts import render
from .forms import UserInputForm
from django.core.mail import send_mail


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


def generate_password(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            # Обработка введенных данных
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Далее - генерация пароля и сохранение в базе данных
            generated_password = "ваш_сгенерированный_пароль"

            # Сохранение в базе данных
            UserGeneratedPassword.objects.create(name=name, email=email, generated_password=generated_password)

            # Отправка сгенерированного пароля на email
            send_mail(
                'Ваш сгенерированный пароль',
                f'Ваш пароль: {generated_password}',
                'от_какого_адреса',
                [email],
                fail_silently=False,
            )

            # Увеличение счетчика генераций в базе данных
            stats = PasswordGenerationStats.objects.first()
            stats.generation_count += 1
            stats.save()
    else:
        form = UserInputForm()

    return render(request, 'generate_password.html', {'form': form})
