from django.shortcuts import render
from XpenCntrl.models import Category 
from django.views.generic import ListView

# Create your views here.

def xpencntrl_index(request):

    return render(request, 'index.html')

def category_list(request):
    data = {
        'title':'Listado de categorías',
        'categories':Category.objects.all()
    }
    return render(request, 'categoria/list.html',data)

class CategoryListView(ListView):
    model = Category
    template = '/categoria/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context
