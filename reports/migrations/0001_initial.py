# Generated by Django 4.0.1 on 2022-03-10 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('executives', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DARTask',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Mark as Deleted')),
                ('visit_date', models.DateField(verbose_name='Visiting date')),
                ('check_in', models.DateTimeField(blank=True, null=True)),
                ('check_out', models.DateTimeField(blank=True, null=True)),
                ('available_time', models.PositiveIntegerField(default=1)),
                ('is_completed', models.BooleanField(default=False)),
                ('time_taken', models.PositiveIntegerField(default=0)),
                ('creator', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('executive', models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.CASCADE, to='executives.salesexecutive')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.shop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DARReschedule',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Mark as Deleted')),
                ('reschedule_date', models.DateField(verbose_name='Reschedule date')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('dar', models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.CASCADE, to='reports.dartask')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DARNotes',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Mark as Deleted')),
                ('title', models.CharField(max_length=221)),
                ('note', models.CharField(blank=True, max_length=221, null=True)),
                ('creator', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('dar', models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.CASCADE, to='reports.dartask')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]