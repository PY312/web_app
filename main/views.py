from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Главная страница!!',
        'values': ['some', 'hello', '123'],
        'obj' : {
            'car' : 'BMW',
            'age': '18',
            'hobby': 'programming'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
