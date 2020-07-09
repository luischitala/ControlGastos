from django.shortcuts import render

# Create your views here.

def xpencntrl_index(request):

    return render(request, 'home.html')