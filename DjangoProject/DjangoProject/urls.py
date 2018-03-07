
from django.contrib import admin
from django.urls import path
from liberary import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', admin.site.urls),

]
urlpatterns += [
    path('books/', views.book_view, name='books'),
    path('books/books/<int:pk>', views.book_detail, name='book-detail'),
]
