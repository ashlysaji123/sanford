# Generated by Django 4.0.3 on 2022-03-22 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_expenseapproval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenseapproval',
            name='title',
        ),
    ]
