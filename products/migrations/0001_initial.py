
from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import uuid
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Mark as Deleted')),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=128, unique=True)),
                ('icon', versatileimagefield.fields.VersatileImageField(upload_to='images/products/categories/icon/', verbose_name='Category Icon')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/products/categories/image/', verbose_name='Category Image')),
                ('creator', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Mark as Deleted')),
                ('name', models.CharField(max_length=128)),
                ('barcode', models.CharField(max_length=128, unique=True)),
                ('item_number', models.CharField(max_length=128, unique=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('list_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('primary_image', versatileimagefield.fields.VersatileImageField(upload_to='images/products/products/primary_image/', verbose_name='Primary Product Image')),
                ('feature_graphic', versatileimagefield.fields.VersatileImageField(upload_to='images/products/products/feature_graphic/', verbose_name='Feature Graphic Image')),
                ('is_hot_product', models.BooleanField(default=False, verbose_name='Mark as Hot Product')),
                ('is_new_arrival', models.BooleanField(default=False, verbose_name='Mark as New Arrival')),
                ('is_out_of_stock', models.BooleanField(default=False, verbose_name='Mark as Out of Stock')),
                ('product_pdf', models.FileField(blank=True, null=True, upload_to='')),
                ('available_regions', models.ManyToManyField(limit_choices_to={'is_deleted': False}, related_name='product_availableregions', to='core.region')),
                ('creator', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Mark as Deleted')),
                ('code', models.CharField(max_length=128, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('category', models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory_category', to='products.category')),
                ('creator', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sub Category',
                'verbose_name_plural': 'Sub Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductWishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product WishList',
                'verbose_name_plural': 'Product WishList items',
            },
        ),
        migrations.CreateModel(
            name='ProductSpecialPrice',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Mark as Deleted')),
                ('special_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('creator', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.PROTECT, to='products.product')),
                ('shop', models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.PROTECT, to='core.shop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Mark as Deleted')),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=128, unique=True)),
                ('icon', versatileimagefield.fields.VersatileImageField(upload_to='images/products/productgroup/icon/', verbose_name='Product Group Icon')),
                ('creator', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.CASCADE, related_name='product_productgroup', to='products.productgroup'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.CASCADE, related_name='product_subcategory', to='products.subcategory'),
        ),
    ]
