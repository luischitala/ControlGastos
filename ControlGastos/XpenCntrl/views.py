from django.shortcuts import redirect, render
from XpenCntrl.models import Category 
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'name':'Luis'}
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context
