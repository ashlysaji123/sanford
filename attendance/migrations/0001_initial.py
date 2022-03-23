

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('working_hours', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('missing_hours', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_leave', models.BooleanField(default=False)),
                ('is_late', models.BooleanField(default=False)),
                ('user', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Mark as Deleted')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('check_in_time', models.TimeField(blank=True, null=True)),
                ('check_out_time', models.TimeField(blank=True, null=True)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('late_reason', models.TextField(blank=True, help_text='add additional information for being late', null=True, verbose_name='Reason for being Late')),
                ('is_leave', models.BooleanField(default=False)),
                ('working_hours', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('creator', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
