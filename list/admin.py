from django.contrib import admin
from .models import List

@admin.register(List)
class FlavorAdmin(admin.ModelAdmin):  
    list_display = ('id', 'title',)
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ('id',)
