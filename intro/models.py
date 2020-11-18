from django.db import models

# Create your models here.

class Post(models.Model):
    def __str__(self):
        if self.user:
            return f'{self.user.get_username()}: {self.body}'

        return f'{self.body}'