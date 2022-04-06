import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from loans.models import Loan,LoanLog
from .serializers import CreateLoanSerializer, LoanListSerializer,LoanLogListSerializer,CreateLoanLogSerializer

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

"""
views for tracking loan payments logs 
"""
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_loan_payments(request,pk):
    serializer = CreateLoanLogSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        loan = Loan.objects.get(pk=pk)
        user = request.user
        """ updating loan payment data """
        amount = serializer.validated_data["amount"]
        loan.paid_amount += amount
        if loan.amount == loan.paid_amount:
            loan.is_returned_completely = True
        loan.save()

        serializer.save(loan=loan,creator=user)
        response = {"message": "Loan Payment Added"}
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        response = {"status": 400, "message": serializer.errors}
        return Response(response, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_loan_logs(request,pk):
    loan = Loan.objects.get(pk=pk)
    queryset = LoanLog.objects.filter(is_deleted=False,loan=loan).order_by("-created")
    serializer = LoanLogListSerializer(
        queryset, context={"request": request}, many=True, read_only=True
    )
    response = {
        "status": 200,
        "data": serializer.data,
    }
    return Response(response, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def loan_log_single(request,pk):
    instance = LoanLog.objects.get(pk=pk).order_by("-created")
    serializer = LoanLogListSerializer(
        instance, context={"request": request}
    )
    response = {
        "status": 200,
        "data": serializer.data,
    }
    return Response(response, status=status.HTTP_200_OK)




   
