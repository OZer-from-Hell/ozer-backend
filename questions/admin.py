from django.contrib import admin
from .models import Qustions

@admin.register(Qustions)
class FlavorAdmin(admin.ModelAdmin):  
    list_display = ('id', 'list', 'order','content', 'answer', 'no1', 'no2','no3','no4',)
    list_filter = ('list',)
    search_fields = ('content',)
    ordering = ('list','order',)