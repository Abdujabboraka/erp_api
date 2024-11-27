from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Fan nomi")
    description = models.TextField(verbose_name="Fan haqida ma'lumot", blank=True, null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ism")
    last_name = models.CharField(max_length=100, verbose_name="Familiya")
    email = models.EmailField(verbose_name="Email")
    subjects = models.ManyToManyField(Subject, related_name="students", verbose_name="Fanlar")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
