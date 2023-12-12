from django.db import models
from author.models import Author
# Create your models here.
class Book(models.Model):   
    title = models.CharField(max_length=40)
    release_at = models.DateField(auto_created=True, null=True)
    genre = models.CharField(max_length=10)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='book'
    )

    def __str__(self) -> str:
        return f'{self.title} -> {self.genre}'

