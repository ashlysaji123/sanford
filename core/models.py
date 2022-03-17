import uuid

from django.db import models
from django.urls import reverse
from location_field.models.plain import PlainLocationField
from django.core.validators import MinValueValidator

class BaseModel(models.Model):
    BOOL_CHOICES = ((True, "Yes"), (False, "No"))

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True
    )
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        "accounts.User",
        limit_choices_to={"is_active": True},
        blank=True,
        null=True,
        related_name="creator_%(class)s_objects",
        on_delete=models.CASCADE,
    )
    is_deleted = models.BooleanField(
        "Mark as Deleted", default=False, choices=BOOL_CHOICES
    )

    class Meta:
        abstract = True


class Year(BaseModel):
    name = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse("core:view_year", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("core:update_year", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("core:delete_year", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)


class Language(BaseModel):
    family = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    native_name = models.CharField(max_length=128, blank=True, null=True)
    lang_code = models.CharField(max_length=128, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("core:view_language", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("core:update_language", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("core:delete_language", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)


class Region(BaseModel):
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("core:view_region", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("core:update_region", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("core:delete_region", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)


class Country(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, blank=True, null=True)
    country_code = models.CharField(max_length=128, blank=True, null=True)
    region = models.ForeignKey(
        Region,
        blank=True,
        null=True,
        limit_choices_to={"is_deleted": False},
        on_delete=models.PROTECT,
        related_name="region",
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def get_absolute_url(self):
        return reverse("core:view_country", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("core:update_country", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("core:delete_country", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)


class State(BaseModel):
    TYPE_CHOICES = (
        ("EMIRATE", "EMIRATE"),
        ("STATE", "STATE"),
        ("UNION TERRITORY", "UNION TERRITORY"),
    )

    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128, default="STATE", choices=TYPE_CHOICES)
    country = models.ForeignKey(
        Country,
        blank=True,
        null=True,
        limit_choices_to={"is_deleted": False},
        on_delete=models.PROTECT,
        related_name="state_country",
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    state_code = models.CharField(max_length=21, blank=True, null=True)
    tin_number = models.CharField(max_length=21, blank=True, null=True)

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("core:view_state", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("core:update_state", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("core:delete_state", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)

    @property
    def country_name(self):
        return self.country.name


class BlockedIP(BaseModel):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return str(f"{self.ip_address}")


class Shop(BaseModel):
    name = models.CharField(max_length=128)
    location = PlainLocationField(based_fields=["city"], zoom=1)
    contact_number = models.CharField(max_length=18)
    contact_number2 = models.CharField(max_length=18, blank=True, null=True)
    country = models.ForeignKey(
        Country,
        blank=True,
        null=True,
        limit_choices_to={"is_deleted": False},
        on_delete=models.PROTECT,
    )
    state = models.ForeignKey(
        State,
        blank=True,
        null=True,
        limit_choices_to={"is_deleted": False},
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("core:view_shop", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("core:update_shop", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("core:delete_shop", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)

    @property
    def country_name(self):
        return self.country.name

