from django.urls import path

from . import views

app_name = 'comic'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:book_url>/', views.book, name='book'),
    path('<slug:book_url>/<slug:chapter_url>/', views.chapter, name='chapter'),
    path('<slug:book_url>/<slug:chapter_url>/<int:page_number>/', views.page, name='page'),
]