from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name
