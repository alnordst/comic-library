from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Book, Chapter, Page


def index(request):
    book_list = Book.objects.all()
    context = {'book_list': book_list}
    return render(request, 'comic/select_book.html', context)
    
def book(request, book_url):
    the_book = Book.objects.filter(book_url = book_url)[0]
    chapter_list = Chapter.objects.select_related().filter(book_id = the_book.id)
    context = {'the_book': the_book, 
               'chapter_list': chapter_list}
    return render(request, 'comic/select_chapter.html', context)
    
def chapter(request, book_url, chapter_url):
    the_book = Book.objects.filter(book_url = book_url)[0]
    the_chapter = Chapter.objects.select_related().filter(book_id = the_book.id, chapter_url = chapter_url)[0]
    page_list = Page.objects.select_related().filter(chapter_id = the_chapter.id)
    context = {'the_book': the_book,
               'the_chapter': the_chapter,
               'page_list': page_list}
    return render(request, 'comic/select_page.html', context)

def page(request, book_url, chapter_url, page_number):
    the_book = Book.objects.filter(book_url = book_url)[0]
    the_chapter = Chapter.objects.select_related().filter(book_id = the_book.id, chapter_url = chapter_url)[0]
    the_page = Page.objects.select_related().filter(chapter_id = the_chapter.id, page_number = page_number)[0]
    context = {'the_book': the_book,
               'the_chapter': the_chapter,
               'page_number': page_number}
    return render(request, 'comic/display_page.html', context)