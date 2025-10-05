from django.shortcuts import render
from .forms import DieatForm
from fitness.services.prompt import generator_diet
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='user:loginuser')
def diet_views(request):
    form = DieatForm(request.POST or None)
    plan = None

    if request.method == 'POST' and form.is_valid():
        diet = form.save(commit=False)
        diet.user = request.user
        diet.save()
        plan = generator_diet(diet)

    return render(request, 'diet_app/diet.html', {
        'form': form,
        'plan': plan,
    })