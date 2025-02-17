from django.db import models

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email