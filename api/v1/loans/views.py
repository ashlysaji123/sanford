import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from loans.models import Loan
from .serializers import CreateLoanSerializer, LoanListSerializer

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_loan_request(request):
    serializer = CreateLoanSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        user = request.user
        serializer.save(creator=user)
        response = {"message": "Loan Requested successfully"}
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        response = {"status": 400, "message": serializer.errors}
        return Response(response, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_loan_requests(request):
    queryset = Loan.objects.filter(
        is_deleted=False,creator=request.user
    ).order_by("-created")
    serializer = LoanListSerializer(
        queryset, context={"request": request}, many=True, read_only=True
    )
    response = {
        "status": 200,
        "data": serializer.data,
    }
    return Response(response, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def loan_requests(request):
    queryset = Loan.objects.filter(
        is_deleted=False,creator__region=request.user.region
    ).order_by("-created")
    serializer = LoanListSerializer(
        queryset, context={"request": request}, many=True, read_only=True
    )
    response = {
        "status": 200,
        "data": serializer.data,
    }
    return Response(response, status=status.HTTP_200_OK)




   
