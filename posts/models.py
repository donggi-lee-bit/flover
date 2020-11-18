from django.db import models

# Create your models here.
class Keyword(models.Model):
    name = models.CharField(max_length = 20)    

    def __str__(self):
        return f"name : {self.name}"

class FlowerColor(models.Model):
    name = models.CharField(max_length = 20)    

    def __str__(self):
        return f"name : {self.name}"


class FlowerType(models.Model):
    name = models.CharField(max_length = 20)    

    def __str__(self):
        return f"name : {self.name}"


class Item(models.Model):
    name = models.CharField(max_length = 100, null=True)
    info = models.TextField()
    image = models.ImageField(upload_to = 'posts', null = True)
    tagged_keywords = models.ManyToManyField(Keyword, related_name = 'flower_list')
    tagged_colors = models.ManyToManyField(FlowerColor, related_name = 'flower_list')
    tagged_types = models.ManyToManyField(FlowerType, related_name = 'flower_list')
    
    def __str__(self):
        return f"name : {self.name} | info : {self.info}"    

class Shop(models.Model):
    name = models.CharField(max_length = 100)
    location = models.TextField()
    phone = models.IntegerField(null=True)

    def __str__(self):
        return f"name : {self.name} | info : {self.location} | phone: {self.phone}"


