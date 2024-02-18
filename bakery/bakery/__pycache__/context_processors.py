from django.shortcuts import render
from .models import Image

def some_view(request):
    # Get the Image object
    logo = Image.objects.first()  # or however you want to get your logo

    # Create the context dictionary
    context = {'logo': logo}

    # Render the template with the context
    return render(request, 'template.html', context)
