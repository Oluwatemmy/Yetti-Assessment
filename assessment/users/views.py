from django.contrib import messages
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required # Users must be authenticated to view the homepage just as requested
def home(request):
    return render(request, 'users/home.html')

# Register a User
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            fullname = form.cleaned_data.get('username')
            messages.success(request, f"{fullname}, Your account has been created successfully! You can proceed to login.")
            return redirect('login')
    else:
        form= UserRegistrationForm()
    context = {
        'form': form,
        'title': 'Register'
    }
    return render(request, 'users/register.html', context)