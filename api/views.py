from django.shortcuts import render
from . import forms
from django.conf import settings
# from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, "api/index.html")

def upload(request):
    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("form is valid")
            post = form.save(commit=False)
            post.save()
            imageURL = settings.MEDIA_URL + form.instance.image.name

            return render(request, 'api/upload.html',
                                    {'form': form, 'post': post})
        else:
            print("form is not valid")

    form = forms.ImageForm()
    return render(request, 'api/upload.html', {'form': form})
