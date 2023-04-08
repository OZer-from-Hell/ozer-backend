from django.contrib import admin
from .models import Ozer, TotalOzer

@admin.register(Ozer)
class OzerAdmin(admin.ModelAdmin):  
    list_display = ('id', 'list', 'nickname', 'answers', 'score',)
    list_filter = ('list','score',)
    search_fields = ('nickname','score',)
    ordering = ('list','id',)
    
@admin.register(TotalOzer)
class TotalOzerAdmin(admin.ModelAdmin):  
    list_display = ('id', 'list', 'number',)