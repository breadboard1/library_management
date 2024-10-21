from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Borrowing, Book, UserBankAccount
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse
from transactions .models import Transaction

class BorrowingBookView(LoginRequiredMixin, View):
    def post(self, request, id):
        book = get_object_or_404(Book, id=id)

        if Borrowing.objects.filter(account=request.user.account, book=book).exists():
            messages.info(request, "You have already borrowed this book.")
            return redirect('my_books')

        user_balance = request.user.account.balance
        borrowing_price = book.borrowing_price

        if user_balance < borrowing_price:
            messages.warning(request, "Insufficient balance to borrow this book.")
            return redirect('my_books')

        request.user.account.balance -= borrowing_price
        request.user.account.save()
        Borrowing.objects.create(account=request.user.account, book=book)

        Transaction.objects.create(
            account=request.user.account,
            amount=borrowing_price,
            balance_after_transaction=request.user.account.balance,
            transaction_type=2,
        )

        messages.success(request, "You have successfully borrowed the book.")
        return redirect('my_books')


class BorrowedBooksView(LoginRequiredMixin, View):
    def get(self, request):
        borrowed_books = Borrowing.objects.filter(account=request.user.account)

        return render(request, './borrowings/borrowed_books.html', {'borrowed_books': borrowed_books})
