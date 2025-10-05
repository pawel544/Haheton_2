from django.shortcuts import render, redirect
from .forms import RegistrateForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='menu_app:menu')
    if request.method=='POST':
        form= RegistrateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='user:loginuser')
        else:
            return render(request, 'user/signup.html', context={'form':form})
    return render(request, 'user/signup.html', context={'form':RegistrateForm()})

def loginuser(request):

    if request.user.is_authenticated:
        return redirect('menu_app:menu')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Nieprawidłowa nazwa użytkownika lub hasło 😕")
            return redirect('user:loginuser')
        login(request, user)
        messages.success(request, f"Witaj ponownie, {user.username}! 👋")
        return redirect('menu_app:menu')


    return render(request, 'user/login.html', {'form': LoginForm()})
@login_required
def logautuser(request):
    logout(request)
    return redirect(to='user:loginuser')


