from django.db import models


# Create your models here.

class tweet(models.Model):
    nickname = models.CharField(max_length=15)
    message = models.CharField(max_length=130)

    def __str__(self):
        return f"nickname: {self.nickname} message: {self.message} "