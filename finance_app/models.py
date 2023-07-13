from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.FloatField()

    def __str__(self):
        return self.name


class Transaction(models.Model):
    # Foreign keys
    # Using models.CASCADE so when the reference object is deleted, the objects with a FK to it are deleted as well
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    # Fields
    amount = models.FloatField()
    date = models.DateTimeField("date added")
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.description
