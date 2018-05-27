from django.db import models


class Book(models.Model):
    # book_id : The url block for this book => /book_id/chapter_id/page_number/
    book_id = models.SlugField(max_length=20) #make unique
    # book_title : The plaintext title displayed to readers
    book_title = models.CharField(max_length=100)

class Chapter(models.Model):
    # book : The book this chapter belongs to
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # chapter_id : The url block for this chapter (see book_id)
    chapter_id = models.SlugField(max_length=20) #make unique
    # chapter_number : Defines order of chapters
    chapter_number = models.IntegerField()
    # chapter_title : The plaintext title displayed to readers
    chapter_title = models.CharField(max_length=100)

class Page(models.Model):
    # chapter : The chapter this page belongs to
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    # page_number : Sets page order and url
    page_number = models.IntegerField()
    # publish_date : Date this page is published
    publish_date = models.DateTimeField()
