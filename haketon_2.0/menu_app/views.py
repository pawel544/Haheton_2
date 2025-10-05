from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='user:loginuser')
def menu(request):
    return render(request, 'menu_app/menu.html')