from django.db import models


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallrey/')
    image_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.image_name