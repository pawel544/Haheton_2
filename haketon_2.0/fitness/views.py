from django.shortcuts import render, redirect
from .forms import GymForms
from .models import Gym
from .services.prompt import generator_gym
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='user:loginuser')
def training_view(request):
    form = GymForms(request.POST or None)
    plan = None

    if request.method == 'POST' and form.is_valid():
        gym = form.save(commit=False)
        gym.user = request.user
        gym.save()
        plan = generator_gym(gym)

    return render(request, 'fitness/index.html', {
        'form': form,
        'plan': plan,
    })