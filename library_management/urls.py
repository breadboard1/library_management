from django.contrib import admin
from django.urls import path, include
from core.views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:category_slug>/', HomeView.as_view(), name = 'category_wise_books'),
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('transactions.urls')),
    path('books/', include('book.urls')),
    path('borrowings/', include('borrowings.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)