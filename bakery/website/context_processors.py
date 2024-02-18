from .models import Image

def logo(request):
    logo = Image.objects.all() 
    return {'logo': logo}
