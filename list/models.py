from django.db import models


class List(models.Model):   
    
    title = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.title
