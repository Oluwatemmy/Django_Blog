from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}, {self.title}"
    

class BlogPosts(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return f"{self.title}"