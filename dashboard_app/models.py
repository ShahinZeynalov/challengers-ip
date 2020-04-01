from django.db import models

# Create your models here.

class Badge(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='badges')
    description = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.created_at}'
