from django.db import models

# Create your models here.

    
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    text = models.CharField(null=True, max_length=100)
    def __str__(self) -> str:
       return self.text
     
class Home_page(models.Model):
  name = models.CharField(max_length =100)
  description = models.TextField(null=True, blank=True)
  image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
  def __str__(self) -> str:
       return self.name
  
  

class cake_type(models.Model):
    name =models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(null=True,blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self) -> str:
       return self.name
  
class ourstory(models.Model):
  name = models.CharField(max_length =100)
  description = models.TextField(null=True, blank=True)
  image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
  def __str__(self) -> str:
       return self.name

class order(models.Model):
  name = models.CharField(max_length =100)
  description = models.TextField(null=True, blank=True)
  image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
  def __str__(self) -> str:
       return self.name

class packges(models.Model):
       name = models.CharField(max_length=100)
       image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
       def __str__(self) -> str:
          return self.name

class values(models.Model):
       name = models.CharField(max_length =100)
       description = models.TextField(null=True, blank=True)
       image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
       def __str__(self) -> str:
              return self.name