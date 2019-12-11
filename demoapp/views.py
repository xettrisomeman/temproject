from django.shortcuts import render , redirect
from .forms import form_carousel_one
from .models import Home_carousel_one


def home(request):
    return render(request , 'demoapp/home.html')



def form(request):
    form = form_carousel_one()
    if request.method == 'POST':
        form = form_carousel_one(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    data = {
        'form':form
    }
    return render(request , 'demoapp/imageupload.html' ,data)

def show_images(request):
    model = Home_carousel_one.objects.all()

    data = {
        'posts':model
    }
    return render(request ,'demoapp/show_images.html',data)

