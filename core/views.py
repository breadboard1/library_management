from django.views.generic import ListView
from book.models import Book
from category.models import Category


class HomeView(ListView):
    template_name = 'index.html'
    context_object_name = 'books'
    model = Book

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            return Book.objects.filter(category__slug=category_slug)
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
