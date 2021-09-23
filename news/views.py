from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArticlesForm


# Create your views here.
def news_home(request):
    news = Artiles.objects.order_by('title')
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news')
        else:
            error = "Форма была не верной"

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
