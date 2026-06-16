from django.db import models


class Fine(models.Model):
    name = models.CharField(max_length=40)
    days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
