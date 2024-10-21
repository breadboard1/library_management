from django.db import models
from category.models import Category
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    borrowing_price = models.IntegerField()
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    category = models.ManyToManyField(Category)
    def __str__(self) -> str:
        return self.title



class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.name}'