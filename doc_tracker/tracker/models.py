from django.db import models

class Download(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Download count: {self.count}"