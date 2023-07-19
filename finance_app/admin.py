from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Account, Transaction, Category


class AccountAdmin(admin.ModelAdmin):
    fields = ["name", "balance"]


class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]


class TransactionAdmin(admin.ModelAdmin):
    fields = ["category", "account", "amount", "date", "description"]


admin.site.register(Account, AccountAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)