from django.db import models

# Create your models here.
class Slider(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to="static/main/img",)

    def __str__(self):
        return self.name