from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=40)
    birth_date = models.DateField(null=True)
    aliace = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name }-> {self.aliace}'


