from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='image')
    uploaded_to = models.DateTimeField(auto_now_add=True)