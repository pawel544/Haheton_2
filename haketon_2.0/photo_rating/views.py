from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from .forms import TrainingPhotoForm
from .models import TrainingPhoto
from fitness.services.prompt import generator_photo
from django.contrib.auth.decorators import login_required

@login_required(login_url='user:loginuser')
def upload_training_photo(request):
    result = None
    preview_url = None

    if request.method == 'POST':
        form = TrainingPhotoForm(request.POST, request.FILES)
        if form.is_valid():

            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()


            try:
                result = generator_photo(photo)
                photo.analysis_result = result
                photo.save()
            except Exception as e:
                result = f"Błąd podczas analizy zdjęcia: {e}"


            if photo.image:
                preview_url = photo.image.url

    else:
        form = TrainingPhotoForm()

    return render(request, 'photo_rating/upload_training_photo.html', {
        'form': form,
        'result': result,
        'preview_url': preview_url,
    })