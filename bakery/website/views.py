from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def home(request):
   Home = Home_page.objects.all()
   img = Image.objects.all()
   cake = cake_type.objects.all()
   pack = packges.objects.all()
   about =  values.objects.all()
   
   
   data ={
      
      'Title':Home,
      'img':img,
      'cake':cake,
      'pack':pack,
      'about':about,
      
   }
   return render(request,'home.html',data)

def about(request):
   
   story = ourstory.objects.all()
   img = Image.objects.all()
   pack = packges.objects.all()
   data ={
      'story':story,
      'img':img,
      'pack':pack,
   }
   
   
   return render(request,'about.html',data)

def contact_us(request):
   img = Image.objects.all()
   data ={
      'img':img,
   }
   return render(request,'contact.html',data)

def How_to_order(request):
   guide = order.objects.all()
   img = Image.objects.all()
   data ={
      'guide':guide,
      'img':img,
   }
   
   return render(request,'order.html',data)

