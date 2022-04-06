from django.urls import path
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.pagination import StandardResultsSetPagination
from products.models import Category, Product, ShopGroup, SubCategory

from .serializers import (
    CategorySerializer,
    ShopGroupSerializer,
    ProductSerializer,
    SubCategorySerializer,
)
from .views import AddToWishlist, ProductFilterView, ProductWishListView

app_name = "products"

urlpatterns = [
    path(
        "categories/",
        ListAPIView.as_view(
            queryset=Category.objects.filter(is_deleted=False),
            serializer_class=CategorySerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "subcategories/",
        ListAPIView.as_view(
            queryset=SubCategory.objects.filter(is_deleted=False),
            serializer_class=SubCategorySerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "shop_groups/",
        ListAPIView.as_view(
            queryset=ShopGroup.objects.filter(is_deleted=False),
            serializer_class=ShopGroupSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "products/",
        ListAPIView.as_view(
            queryset=Product.objects.filter(is_deleted=False),
            serializer_class=ProductSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
            filter_backends=[OrderingFilter],
        ),
    ),
    path(
        "hot_products/",
        ListAPIView.as_view(
            queryset=Product.objects.filter(is_deleted=False, is_hot_product=True),
            serializer_class=ProductSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "new_arrivals/",
        ListAPIView.as_view(
            queryset=Product.objects.filter(is_deleted=False, is_new_arrival=True),
            serializer_class=ProductSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "categories/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=Category.objects.filter(is_deleted=False),
            serializer_class=CategorySerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "subcategories/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=SubCategory.objects.filter(is_deleted=False),
            serializer_class=SubCategorySerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "shop_group/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=ShopGroup.objects.filter(is_deleted=False),
            serializer_class=ShopGroupSerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "products/view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=Product.objects.filter(is_deleted=False),
            serializer_class=ProductSerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
    # path(
    #     "wishlist/",
    #     ListAPIView.as_view(
    #         queryset=ProductWishList.objects.filter(user=request.user),
    #         serializer_class=ProductWishListSerializer,
    #         pagination_class=StandardResultsSetPagination,
    #         permission_classes =[IsAuthenticated],
    #         filter_backends = [OrderingFilter],
    #     ),
    # ),
    path("wishlist/", ProductWishListView.as_view()),
    path("add/wishlist/<str:pk>/", AddToWishlist.as_view()),
    path("product-filter/", ProductFilterView.as_view()),
    # path('product-filter',product_filtering),
]
