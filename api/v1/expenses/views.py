import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from expenses.models import Expenses

from .serializers import CreateExpensesSerializer,ExpensesListSerializer

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_expenses(request):
    serializer = CreateExpensesSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        serializer.save(user=request.user, creator=request.user)
        response = {"message": "Successfully Submitted."}
        return Response(response, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_expenses(request):
    queryset = Expenses.objects.filter(
        user=request.user,is_deleted=False
    ).order_by("-created")

    serializer = ExpensesListSerializer(
        queryset, context={"request": request}, many=True, read_only=True
    )
    response = {
        "status": 200,
        "data": serializer.data,
    }
    return Response(response, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_expenses(request, pk):
    Expenses.objects.filter(pk=pk,user=request.user).update(is_deleted=True)
    response = {"message": "Successfully Deleted."}
    return Response(response, status=status.HTTP_200_OK)
    
