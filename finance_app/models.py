from django.db import models
import datetime


class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.FloatField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    # Foreign keys
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories_key')
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='accounts_key')
    # Fields
    amount = models.FloatField()
    date = models.DateTimeField("date added")
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.description
