from django.db import models

# Create your models here.

class rUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=300)
    user_password = models.CharField(max_length=30)
    user_phone = models.CharField(max_length=20)
    user_country = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name