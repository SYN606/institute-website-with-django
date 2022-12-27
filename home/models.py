from django.db import models


class User(models.Model):

    name = models.CharField(max_length=100, null=False)
    ph_number = models.IntegerField(default=0)
    email = models.EmailField(
        max_length=254,
    )
    query = models.TextField()

    def __str__(self):
        return "%s %s" % (self.name, self.ph_number)
