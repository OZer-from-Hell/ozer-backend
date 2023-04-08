from django.db import models


class Qustions(models.Model):   
    list = models.ForeignKey('list.List', related_name='questions', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(blank=False, null=False)
    content = models.CharField(max_length=255, blank=False, null=False)
    answer = models.PositiveIntegerField(blank=False, null=False)
    no1 = models.CharField(max_length=50, blank=False, null=False)
    no2 = models.CharField(max_length=50, blank=False, null=False)
    no3 = models.CharField(max_length=50, blank=False, null=False)
    no4 = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return f'{self.order}-{self.content}'
