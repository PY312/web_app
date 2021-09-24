from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Artiles
    template_name = 'news/create.html'

    # fields = ['title', 'anons', 'full_text', 'date']
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Artiles
    success_url = '/news'
    template_name = 'news/news-delete.html'


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
