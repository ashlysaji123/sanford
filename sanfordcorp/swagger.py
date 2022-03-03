
from collections import OrderedDict

from drf_yasg import openapi
from drf_yasg.inspectors import PaginatorInspector
from drf_yasg.views import get_schema_view
from rest_framework import permissions


class PageNumberPaginatorInspectorClass(PaginatorInspector):
    def get_paginated_response(self, paginator, response_schema):
        paged_schema = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=OrderedDict((
                ('count', openapi.Schema(type=openapi.TYPE_INTEGER)),
                ('elements', openapi.Schema(type=openapi.TYPE_INTEGER)),
                ('results', response_schema),
            )),
            required=['results']
        )

        return paged_schema


schema_view = get_schema_view(
	openapi.Info(title="Sanford Corp API Documentation", default_version="v1.0"),
	public=True,
	permission_classes =[permissions.AllowAny],
)
