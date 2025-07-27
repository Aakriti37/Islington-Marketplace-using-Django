from django.db import models
# from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    category = models.CharField(max_length=100, default='Untitled')
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)


    def __str__(self):
        return self.title
    
