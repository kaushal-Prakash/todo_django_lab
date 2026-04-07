from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('publishers/add/', views.add_publisher, name='add_publisher'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/add/', views.add_author, name='add_author'),
]