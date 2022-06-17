from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField("이름", max_length=50)
    description = models.TextField("설명")

    def __str__(self):
        return self.name
