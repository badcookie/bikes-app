from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Motobike(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, db_column='category', on_delete=models.CASCADE, to_field='name'
    )
    company = models.ForeignKey(
        Company, db_column='company', on_delete=models.CASCADE, to_field='name'
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
