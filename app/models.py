from django.db import models


class User_grade(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    grade = models.DecimalField(max_digits=8,decimal_places=2)


