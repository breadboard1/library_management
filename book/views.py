from django.views.generic import DetailView
from transactions .models import Transaction
from django.contrib import messages
from . import models
from . import forms
from borrowings .models import Borrowing

class DetailBookView(DetailView):
    model = models.Book
    pk_url_kwarg = "id"
    template_name = "./book/book_details.html"

    def post(self, request, *args, **kwargs):
        review_form = forms.ReviewForm(data=request.POST)
        self.object = self.get_object()

        has_borrowed = Borrowing.objects.filter(book=self.object, account__user=request.user).exists()

        if review_form.is_valid() and has_borrowed:
            review = review_form.save(commit=False)
            review.book = self.object
            review.save()
            messages.success(request, "Thank you for your review!")
        else:
            messages.error(request, "You must borrow the book to submit a review.")

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        reviews = book.reviews.all()
        review_form = forms.ReviewForm()

        has_borrowed = False
        if self.request.user.is_authenticated:
            has_borrowed = Borrowing.objects.filter(book=book, account__user=self.request.user).exists()

        context['reviews'] = reviews
        context['review_form'] = review_form
        context['has_borrowed'] = has_borrowed
        return context