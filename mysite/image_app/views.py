from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from django.shortcuts import render, redirect
from .forms import *
from .models import Cats
  
def upload_image(request): 
    if request.method == 'POST': 
        form = catform(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
            return redirect('display_images')
    else: 
        form = catform()
    return render(request, 'upload_image.html', {'form' : form}) 


def display_images(request):
    if request.method == 'GET': 
        # getting all the objects of cats. 
        cat_images = Cats.objects.all();
        return render(request, 'display_images.html', 
            {'cat_images' : cat_images})


