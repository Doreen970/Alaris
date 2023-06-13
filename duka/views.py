from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm
from django.contrib.auth import logout as my_logout
from django.http import HttpResponse

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request, 'duka/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'duka/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()   

    return render(request, 'duka/signup.html', {
        'form': form
    }) 

def my_logout(request):
    if request.method == 'POST':
        logout(request)

        return redirect('index') 

    return HttpResponse("Logoutpage")          