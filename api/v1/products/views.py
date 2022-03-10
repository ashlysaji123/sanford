from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.core.utils import get_res_data
from core.pagination import StandardResultsSetPagination
from products.models import Product, ProductWishList

from .serializers import ProductSerializer, ProductWishListSerializer

# def product_filtering(request):
#     query = request.GET.get('q')
#     queryset = Product.objects.filter(is_deleted=False)

#     # paginator = PageNumberPagination()
#     if query:
#         queryset = queryset.filter(
#             Q(name__icontains=query) |
#             Q(subcategory__category__icontains=query)
#         )

# result_page = paginator.paginate_queryset(queryset, request)
# serializer = PostListSerializer(
#     result_page, context={"request": request}, many=True, read_only=True)
# data = serializer.data


# return paginator.get_paginated_response(data)


class ProductFilterView(ListAPIView):
    """
    fetching list of Product using filters
    """

    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("name", "subcategory__category", "barcode", "item_number")
    ordering_fields = ("name", "created", "-name", "list_price", "-list_price")
    search_fields = ("name", "barcode", "item_number")


class ProductWishListView(APIView):
    """
    List wishlist products based on user, or create a new Wishlist product.
    """

    queryset = ProductWishList.objects.all()
    serializer_class = ProductWishListSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        wishlist = ProductWishList.objects.filter(user=request.user)
        serializer = ProductWishListSerializer(wishlist, many=True)
        return Response(serializer.data)




class AddToWishlist(APIView):
    def get_object(self, pk):
        # Returns an object instance that should
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        product = self.get_object(pk)
        if not ProductWishList.objects.filter(
            user=request.user, product=product
        ).exists():
            wishlist_item = ProductWishList.objects.create(
                product=product,
                user=request.user,
            )
            wishlist_item.save()
            response = get_res_data(200, "Added Successfully!.")
            return Response(response, status=status.HTTP_200_OK)
        else:
            ProductWishList.objects.filter(user=request.user, product=product).delete()
            response = get_res_data(200, "Removed Successfully!.")
            return Response(response, status=status.HTTP_200_OK)
