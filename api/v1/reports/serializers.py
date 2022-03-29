from rest_framework import serializers

from products.models import Product
from reports.models import CollectMoney,Order,OrderItem,DARTask, UploadPhoto,DARNotes

class DARTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DARTask
        fields = ('executive','shop','pk','visit_date','check_in','check_out','available_time','time_taken')


class DARListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DARNotes
        fields = ('DAR_TYPES','dar','pk','note','type','is_completed')

    
class CreateCollectMoneySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CollectMoney
        fields = ('total_credit_amount', 'received_money','dar_note')


class CreateOrderItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = OrderItem
        fields = ("id", "qty", "product")
        read_only_fields = ("order",)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("qty", "product", "creator", "pk", "total_items_amount", "order")


class CreateOrderSerializer(serializers.ModelSerializer):
    order_items = CreateOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ("order_items",)

    def create(self, validated_data):
        order_items_data = validated_data.pop("order_items")
        order = Order.objects.create(**validated_data)
        total_amount = 0
        for item in order_items_data:
            qty = item["qty"]
            item_product = item["product"]
            # any  item logic here
            product = Product.objects.get(pk=item_product.pk)
            product_price = product.list_price
            total_items_amount = product_price * qty
            OrderItem.objects.create(
                order=order,
                total_items_amount=total_items_amount,
                **item
            )
            total_amount += total_items_amount
        order.total_amount = total_amount
        order.save()
        return order
    

class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            "dar_note",
            "pk",
            "total_amount",
            "advanced_amount"
        )

    def get_order_items(self, obj):
        order_items = OrderItem.objects.filter(sale=obj)
        return OrderItemSerializer(order_items, many=True).data



class UploadPhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UploadPhoto
        fields = ('image1','image2','image3')
