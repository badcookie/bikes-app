from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Motobike(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
