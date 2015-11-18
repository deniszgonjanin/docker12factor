from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Comment

# Create your views here.
def index(request):
    comments = Comment.objects.order_by('-datetime')
    context = {'comments': comments}
    
    return render(request, 'index.html', context)
    
def post(request):
    comment = Comment(comment=request.POST['content'])
    comment.save()
    
    return HttpResponseRedirect(reverse('index'))