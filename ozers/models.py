from django.db import models


class Ozer(models.Model):   
    list = models.ForeignKey('list.List', related_name='ozers', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, blank=False, null=False, unique=True)
    answers = models.CharField(max_length=255, blank=True, null=True)
    score = models.PositiveIntegerField(default=0, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.nickname

class TotalOzer(models.Model): 
    list = models.ForeignKey('list.List', on_delete=models.CASCADE)
    number = models.CharField(max_length=20, blank=False, null=False, unique=True)
    
    def __str__(self):
        return f'{self.list}-{self.number}'