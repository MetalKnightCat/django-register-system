from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def user_list(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password', None)

        # Validate passwords match (for registration)
        if confirm_password and password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('user_list')

        try:
            User.objects.create(email=email, password=password)
            messages.success(request, "User created successfully!")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")

        return redirect('user_list')

    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})