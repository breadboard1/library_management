from django.db import models
from accounts.models import UserBankAccount
from book.models import Book

class Borrowing(models.Model):
    account = models.ForeignKey(UserBankAccount, related_name = 'borrower', on_delete = models.CASCADE)
    book = models.ForeignKey(Book, related_name='borrowed_book', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __self__(self):
        return f"{self.book.title}"