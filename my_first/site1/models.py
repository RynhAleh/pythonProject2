from django.db import models


# Create your models here.
class Model1 (models.Model):
    firstname = models.CharField(max_length=45, default="")
    lastname = models.CharField(max_length=45, default="")
    age = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.age}'
