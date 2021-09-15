from django.db import models

# Create your models here.

class gadgets(models.Model):

    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='media')
    Year = models.CharField(max_length=50)
    Price = models.IntegerField()