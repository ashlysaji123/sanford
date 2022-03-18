from itertools import product
from rest_framework import serializers

from products.models import Product
from api.v1.products.serializers import ProductSerializer
from votings.models import (
    VotingItem,
    Voting
)


class VotingItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    perfect_count = serializers.SerializerMethodField()
    good_count = serializers.SerializerMethodField()
    bad_count = serializers.SerializerMethodField()
    

    class Meta:
        model = VotingItem
        fields = ('pk',"product", "voting_startdate", "voting_enddate", "perfect_count", "good_count", "bad_count")

    def get_product(self, obj):
        product = Product.objects.get(pk=obj.product.pk)
        return ProductSerializer(product).data

    def get_perfect_count(self, obj):
        perfect_count = Voting.objects.filter(voting="perfect").count()
        return perfect_count

    def get_good_count(self, obj):
        good_count = Voting.objects.filter(voting="good").count()
        return good_count

    def get_bad_count(self, obj):
        bad_count = Voting.objects.filter(voting="bad").count()
        return bad_count


class VotingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Voting
        fields = ("voting",)



