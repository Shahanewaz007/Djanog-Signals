from django.shortcuts import render, redirect
from django.contrib import messages
from .signals import user_registered
from .models import User


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('signup')

        user = User.objects.create(username=username, email=email, password=password)
        user_registered.send(sender=None, user=user, request=request)

        return redirect('home')

    return render(request, 'signup.html')
