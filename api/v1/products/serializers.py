from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from api.v1.core.serializers import RegionSerializer
from products.models import Category, Product, ProductGroup, SubCategory,ProductWishList


class CategorySerializer(serializers.ModelSerializer):
    icon = VersatileImageFieldSerializer(sizes=[("full_size", "url"), ("thumbnail", "thumbnail__800x400")])
    image = VersatileImageFieldSerializer(sizes=[("full_size", "url"), ("thumbnail", "thumbnail__800x400")])

    class Meta:
        model = Category
        fields = ("pk", "code", "name", "icon", "image")


class SubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField()

    class Meta:
        model = SubCategory
        fields = ("pk", "code", "name", "category", "category_name")


class ProductGroupSerializer(serializers.ModelSerializer):
    subcategory_name = serializers.ReadOnlyField()

    class Meta:
        model = ProductGroup
        fields = ("pk", "name", "code", "icon", "subcategory_name")


class ProductSerializer(serializers.ModelSerializer):
    group_name = serializers.ReadOnlyField()
    subcategory_name = serializers.ReadOnlyField()
    available_regions = RegionSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = (
            "pk","name", "barcode", "item_number", "summary", "description", "group", "group_name", "subcategory", "subcategory_name","product_pdf",
            "list_price", "primary_image", "feature_graphic", "is_hot_product", "is_new_arrival", "is_out_of_stock", "available_regions", 
        )


class ProductWishListSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = ProductWishList
        fields = ('product',)

    def get_product(self,obj):
        product = Product.objects.get(pk=obj.product.pk)
        print(product,".....")
        return ProductSerializer(product).data
