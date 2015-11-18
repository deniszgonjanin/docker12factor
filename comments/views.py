from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def index(request):
    comments = Comment.objects.order_by('-datetime')
    context = {'comments': comments}
    
    return render(request, 'index.html', context)