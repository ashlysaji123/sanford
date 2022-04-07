from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from api.v1.core.serializers import RegionSerializer,ShopSerializer
from products.models import (
    Category,
    Product,
    ShopGroup,
    ProductWishList,
    SubCategory,
)


class CategorySerializer(serializers.ModelSerializer):
    icon = VersatileImageFieldSerializer(
        sizes=[("full_size", "url"), ("thumbnail", "thumbnail__800x400")]
    )
    image = VersatileImageFieldSerializer(
        sizes=[("full_size", "url"), ("thumbnail", "thumbnail__800x400")]
    )

    class Meta:
        model = Category
        fields = ("pk", "code", "name", "icon", "image")


class SubCategorySerializer(serializers.ModelSerializer):
    group_name = serializers.SerializerMethodField()

    class Meta:
        model = SubCategory
        fields = ("pk", "code", "name", "group", "group_name")
    
    def get_group_name(self,obj):
        return obj.group.name



class ShopGroupSerializer(serializers.ModelSerializer):
    shops = ShopSerializer(read_only=True, many=True)
    class Meta:
        model = ShopGroup
        fields = ("pk", "name", "region", "shops")


class ProductSerializer(serializers.ModelSerializer):
    subcategory_name = serializers.ReadOnlyField()
    available_regions = RegionSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = (
            "pk",
            "name",
            "retail_barcode",
            "ecommerse_barcode",
            "item_number",
            "summary",
            "description",
            "subcategory",
            "subcategory_name",
            "product_pdf",
            "list_price",
            "primary_image",
            "feature_graphic",
            "is_hot_product",
            "is_new_arrival",
            "is_out_of_stock",
            "available_regions",
        )


class ProductWishListSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = ProductWishList
        fields = ("product",)

    def get_product(self, obj):
        product = Product.objects.get(pk=obj.product.pk)
        print(product, ".....")
        return ProductSerializer(product).data
