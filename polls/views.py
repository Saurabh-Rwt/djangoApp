from django.shortcuts import render, redirect
from .forms import UserProfileForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def feed(request):
    return render(request, 'feed.html')

def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
    else:
        form = UserProfileForm()

    return render(request, 'register.html', {'form': form})