from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    photo=models.ImageField(upload_to='photo')
    post_body = models.TextField()
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.title
