from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    membership_start = models.DateField()
    membership_end = models.DateField()
    plan_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name
