from django.contrib import admin

from .models import Account, CustomUser


class AccountAdmin(admin.ModelAdmin):
    fields = ["name", "balance"]


class CustomUserAdmin(admin.ModelAdmin):
    fields = ["email", "username", "password"]


admin.site.register(Account, AccountAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
