from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200,blank=False)
    content = models.TextField(max_length=200,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

# Create your models here.
