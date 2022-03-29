import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from reports.models import DARNotes, DARTask
from .serializers import (
     CreateCollectMoneySerializer,
     DARListSerializer,
     CreateOrderSerializer,
     UploadPhotoSerializer,
     DARTaskSerializer
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def DAR_task(request):
    queryset = DARTask.objects.filter(
        is_deleted=False,
    ).order_by("-created")

    serializer = DARTaskSerializer(
        queryset, context={"request": request}, many=True, read_only=True
    )
    response = {
        "status": 200,
        "data": serializer.data,
    }
    return Response(response, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def DAR_list(request):
    queryset = DARNotes.objects.filter(
        is_deleted=False,
    ).order_by("-created")

    serializer = DARListSerializer(
        queryset, context={"request": request}, many=True, read_only=True
    )
    response = {
        "status": 200,
        "data": serializer.data,
    }
    return Response(response, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_collect_money(request):
    serializer = CreateCollectMoneySerializer(data=request.data,context={"request": request})
    if serializer.is_valid():
        user=request.user
        serializer.save()
        response = {"message": "Collectmoney added successfully"}
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        response = {"status": 400, "message": serializer.errors}
        return Response(response, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_order(request,pk):
    serializer = CreateOrderSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        dar_note = DARNotes.objects.get(pk=pk)
        serializer.save(creator=request.user,dar_note=dar_note)
        response = {"message": "Successfully Submitted."}
        return Response(response, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_upload_photo(request,pk):
    serializer = UploadPhotoSerializer(data=request.data,context={"request": request})
    if serializer.is_valid():
        dar_note = DARNotes.objects.get(pk=pk)
        serializer.save(creator=request.user,dar_note=dar_note)
        response = {"message": "Photo uploaded successfully"}
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        response = {"status": 400, "message": serializer.errors}
        return Response(response, status=status.HTTP_200_OK)