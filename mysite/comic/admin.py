from django.contrib import admin

from .models import Book, Chapter, Page


class ChapterInline(admin.TabularInline):
    model = Chapter
    show_change_link = True
    
    
class PageInline(admin.TabularInline):
    model = Page
    show_change_link = True
    
    
class BookAdmin(admin.ModelAdmin):
    fields = ['book_url', 'book_title']
    inlines = [ChapterInline]

    
    
class ChapterAdmin(admin.ModelAdmin):
    fields = ['chapter_number', 'chapter_url', 'chapter_title']
    inlines = [PageInline]

    

class PageAdmin(admin.ModelAdmin):
    fields = ['page_number', 'publish_date']
    
    
admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
#admin.site.register(Page, PageAdmin)