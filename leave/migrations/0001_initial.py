# Generated by Django 4.0.3 on 2022-03-23 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Mark as Deleted')),
                ('startdate', models.DateField(help_text='leave start date is on ..', verbose_name='Start Date')),
                ('enddate', models.DateField(help_text='coming back on ...', verbose_name='End Date')),
                ('leavetype', models.CharField(choices=[('sick', 'Sick Leave'), ('casual', 'Casual Leave'), ('emergency', 'Emergency Leave'), ('study', 'Study Leave'), ('annual', 'Annual Leave'), ('maternity', 'Maternity Leave'), ('paternity', 'Paternity Leave'), ('bereavement', 'Bereavement Leave'), ('quarantine', 'Self Quarantine'), ('compensatory', 'Compensatory Leave'), ('sabbatical', 'Sabbatical Leave')], default='sick', max_length=25)),
                ('reason', models.TextField(blank=True, help_text='add additional information for leave', null=True, verbose_name='Reason for Leave')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('total_available_leave', models.PositiveIntegerField(default=12)),
                ('leave_duration', models.PositiveIntegerField(default=0)),
                ('manager_approved', models.BooleanField(default=False)),
                ('manager_rejected', models.BooleanField(default=False)),
                ('coordinator_approved', models.BooleanField(default=False)),
                ('coordinator_rejected', models.BooleanField(default=False)),
                ('executive_approved', models.BooleanField(default=False)),
                ('executive_rejected', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
