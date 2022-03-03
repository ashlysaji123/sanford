from rest_framework import serializers

from sales.models import OpeningStock, Sales, SaleItems
from products.models import Product

class OpeningStockSerializer(serializers.ModelSerializer):
    merchandiser_name = serializers.ReadOnlyField(
        source="merchandiser.fullname")
    product_name = serializers.ReadOnlyField(source="product.name")

    class Meta:
        model = OpeningStock
        fields = ("merchandiser", "product", "merchandiser_name",
                  "product_name", "count", 'pk')


class CreateSaleItemsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = SaleItems
        fields = ('id','qty', 'product')
        read_only_fields = ('sale',)

class SaleItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItems
        fields = ('qty', 'product', 'creator','pk','total_items_amount','sale')



class CreateSalesSerializer(serializers.ModelSerializer):
    sale_items = CreateSaleItemsSerializer(many=True)
    class Meta:
        model = Sales
        fields = ('sale_items',)

    def create(self, validated_data):
        sale_items_data = validated_data.pop('sale_items')
        sale = Sales.objects.create(**validated_data)
        total_amount = 0
        for item in sale_items_data:
            qty = item['qty']
            item_product = item['product']
            #any sale item logic here
            product = Product.objects.get(pk=item_product.pk)
            product_price = product.list_price
            total_items_amount = (product_price * qty)
            SaleItems.objects.create(sale=sale,total_items_amount=total_items_amount,creator=sale.user, **item)
            total_amount += total_items_amount
        sale.total_amount = total_amount
        sale.save()
        return sale
    
    def update(self,instance,validated_data):
        print("update view")
        sale_items_data = validated_data.pop('sale_items')
        sale = instance
        keep_items = []
        existing_items = SaleItems.objects.filter(sale=sale)
        for sale_item in sale_items_data:
            #any sale item logic here
            if SaleItems.objects.filter(sale=sale,product=sale_item['product']).exists():
                item = SaleItems.objects.get(sale=sale,product=sale_item['product'])
                item.qty = sale_item.get('qty',item.qty)
                product_price = item.product.list_price
                item.total_items_amount = (product_price * item.qty)
                item.save()
                keep_items.append(item.id)
            else:
                qty = sale_item['qty']
                item_product = sale_item['product']
                #any sale item logic here
                product = Product.objects.get(pk=item_product.pk)
                product_price = product.list_price
                total_items_amount = (product_price * qty)
                item = SaleItems.objects.create(sale=sale,total_items_amount=total_items_amount,creator=sale.user, **item)
                keep_items.append(items.id)
        for i in existing_items:
            if i.id not in keep_items:
                i.delete()
        return instance



class SalesSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    sale_items = serializers.SerializerMethodField()

    class Meta:
        model = Sales
        fields = ('user', 'total_amount', 'photo',
                  'is_approved', 'is_rejected',
                  'user_name', 'sale_items', 'pk'

                  )

    def get_user_name(self, obj):
        if obj.user:
            return obj.user.username

    def get_sale_items(self, obj):
        sale_items = SaleItems.objects.filter(sale=obj)
        return SaleItemsSerializer(sale_items, many=True).data
