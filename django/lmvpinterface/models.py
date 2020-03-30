from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=32)
    create_time = models.DateTimeField('time created')

class Commit(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    hash_val = BinaryField(max_length=49, decimal_places=49) #SHA1 is 160 bits or 49 decimal digits
