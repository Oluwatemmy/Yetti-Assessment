from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'users/home.html')

# Register a User
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            fullname = form.cleaned_data.get('full_name')
            messages.success(request, f"Account created for {fullname}")
            return redirect('homepage')
    else:
        form= UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)