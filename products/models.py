from decimal import Decimal
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField

from core.models import BaseModel, Region


class Category(BaseModel):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128, unique=True)
    icon = VersatileImageField(
        "Category Icon", upload_to="images/products/categories/icon/"
    )
    image = VersatileImageField(
        "Category Image", upload_to="images/products/categories/image/"
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)


class SubCategory(BaseModel):
    category = models.ForeignKey(
        "Category",
        limit_choices_to={"is_deleted": False},
        related_name="subcategory_category",
        on_delete=models.CASCADE,
    )
    code = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return str(self.name)

    @property
    def category_name(self):
        return str(self.category.name)


class ProductGroup(BaseModel):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128, unique=True)
    icon = VersatileImageField(
        "Product Group Icon", upload_to="images/products/productgroup/icon/"
    )

    def __str__(self):
        return str(self.name)


class Product(BaseModel):
    name = models.CharField(max_length=128)
    barcode = models.CharField(max_length=128, unique=True)
    item_number = models.CharField(max_length=128, unique=True)
    summary = models.TextField(blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    group = models.ForeignKey(
        "ProductGroup",
        limit_choices_to={"is_deleted": False},
        related_name="product_productgroup",
        on_delete=models.CASCADE,
    )
    subcategory = models.ForeignKey(
        "SubCategory",
        limit_choices_to={"is_deleted": False},
        related_name="product_subcategory",
        on_delete=models.CASCADE,
    )
    list_price = models.DecimalField(
        default=0.0,
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    available_regions = models.ManyToManyField(
        Region,
        limit_choices_to={"is_deleted": False},
        related_name="product_availableregions",
    )
    primary_image = VersatileImageField(
        "Primary Product Image", upload_to="images/products/products/primary_image/"
    )
    feature_graphic = VersatileImageField(
        "Feature Graphic Image", upload_to="images/products/products/feature_graphic/"
    )
    is_hot_product = models.BooleanField("Mark as Hot Product", default=False)
    is_new_arrival = models.BooleanField("Mark as New Arrival", default=False)
    is_out_of_stock = models.BooleanField("Mark as Out of Stock", default=False)
    product_pdf = models.FileField(blank=True, null=True)
    catalogue_url = models.URLField(max_length=450,blank=True, null=True)

    def __str__(self):
        return str(self.name)

    @property
    def group_name(self):
        return str(self.group.name)

    @property
    def subcategory_name(self):
        return str(self.subcategory.name)


class ProductWishList(models.Model):
    user = models.ForeignKey(
        "accounts.User", limit_choices_to={"is_active": True}, on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product WishList"
        verbose_name_plural = "Product WishList items"

    def __str__(self):
        return self.product.name




class ProductSpecialPrice(BaseModel):
    product = models.ForeignKey(
        Product,
        limit_choices_to={"is_deleted": False},
        on_delete=models.PROTECT,
    )
    shop = models.ForeignKey(
        'core.Shop',
        limit_choices_to={"is_deleted": False},
        on_delete=models.PROTECT,
    )
    special_price = models.DecimalField(
        default=0.0,
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(Decimal("0.00"))],
    )

    def get_absolute_url(self):
        return reverse("products:view_special_price", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("products:update_special_price", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("products:delete_special_price", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.shop.name)

