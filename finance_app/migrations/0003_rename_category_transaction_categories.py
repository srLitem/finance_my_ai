# Generated by Django 4.2.2 on 2023-08-01 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0002_remove_transaction_category_transaction_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='category',
            new_name='categories',
        ),
    ]
