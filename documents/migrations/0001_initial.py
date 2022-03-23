

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
            name='EmployeeDocuments',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Mark as Deleted')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('manager_approved', models.BooleanField(default=False)),
                ('manager_rejected', models.BooleanField(default=False)),
                ('coordinator_approved', models.BooleanField(default=False)),
                ('coordinator_rejected', models.BooleanField(default=False)),
                ('executive_approved', models.BooleanField(default=False)),
                ('executive_rejected', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeDocumentsItems',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Mark as Deleted')),
                ('title', models.CharField(max_length=250)),
                ('image', models.FileField(blank=True, null=True, upload_to='document/')),
                ('creator', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.employeedocuments')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
