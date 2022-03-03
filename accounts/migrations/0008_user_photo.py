# Generated by Django 4.0.1 on 2022-03-03 11:35

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_employ_id_user_employe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='accounts/user/photo/', verbose_name='User Profile Photo'),
        ),
    ]
