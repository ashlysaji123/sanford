import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from documents.models import EmployeeDocumentsItems,EmployeeDocuments
from .serializers import CreateEmployeeDocumentsItemsSerializer, CreateEmployeeDocumentsSerializer,EmployeeDocumentsSerializer



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_documents(request):
    serializer = CreateEmployeeDocumentsSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        serializer.save(user=request.user, creator=request.user)
        response = {"message": "Successfully Submitted."}
        return Response(response, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_document(request, pk):
    instance = EmployeeDocuments.objects.get(pk=pk)
    serializer = CreateEmployeeDocumentsSerializer(
        instance, data=request.data, context={"request": request}
    )
    if serializer.is_valid():
        serializer.save(updater=request.user)
        response = {"message": "Successfully Updated."}
        return Response(response, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_documents(request):
    queryset = EmployeeDocuments.objects.filter(
        is_deleted=False, user=request.user
    )

    serializer = EmployeeDocumentsSerializer(
        queryset, context={"request": request}, many=True, read_only=True
    )

    return Response(serializer.data, status=status.HTTP_200_OK)
