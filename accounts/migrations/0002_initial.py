# Generated by Django 4.0.3 on 2022-03-23 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('products', '0001_initial'),
        ('core', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='favouritegroup',
            name='group',
            field=models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.CASCADE, related_name='accounts_favourite_group', to='products.productgroup'),
        ),
        migrations.AddField(
            model_name='favouritegroup',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.ForeignKey(limit_choices_to={'is_deleted': False}, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.region'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
