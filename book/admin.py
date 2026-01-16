from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'is_available', 'publishdate')

    ordering = ('-published_date', 'title')
    
    list_filter = ('is_available', 'published_date')

    search_fields = ('title', 'description')

    readonly_fields = ('price' , 'publishdate')