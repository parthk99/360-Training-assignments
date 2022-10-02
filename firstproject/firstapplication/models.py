from django.db import models

# Create your models here.
class user (models.Model):
    Name = models.CharField(max_length = 255)
    Address = models.CharField(max_length = 255)
    Contact = models.IntegerField()

    def __str__(self):
        return f'{self.Name} {self.Address} {self.Contact}'