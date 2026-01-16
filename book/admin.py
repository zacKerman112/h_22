from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'is_available', 'publishdate' , 'author' , 'price')

    ordering = ('-published_date', 'title')
    
    list_filter = ('is_available', 'publishdate')

    search_fields = ('title', 'description')

    readonly_fields = ('price' , 'publishdate')