from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Transaction, Category


class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]


class TransactionAdmin(admin.ModelAdmin):
    fields = ["category", "account", "amount", "date", "description"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)