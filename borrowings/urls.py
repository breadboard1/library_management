from django.urls import path
from . import views

urlpatterns = [
    path('borrow/<int:id>/', views.BorrowingBookView.as_view(), name='borrow_book'),
    path('borrow/books/', views.BorrowedBooksView.as_view(), name='my_books'),
]