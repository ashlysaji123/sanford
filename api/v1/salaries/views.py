import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from salaries.models import SalaryAdavance
from .serializers import CreateSalaryAdvanceSerializer, SalaryAdvanceListSerializer

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_salary_advance_request(request):
    serializer = CreateSalaryAdvanceSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        user = request.user
        serializer.save(creator=user,user=user,)
        response = {"message": "Salary Advance Requested successfully"}
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        response = {"status": 400, "message": serializer.errors}
        return Response(response, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_salary_advance_requests(request):
    queryset = SalaryAdavance.objects.filter(
        is_deleted=False, user=request.user
    ).order_by("-created")

    serializer = SalaryAdvanceListSerializer(
        queryset, context={"request": request}, many=True, read_only=True
    )
    response = {
        "status": 200,
        "data": serializer.data,
    }
    return Response(response, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def salary_advance_list(request):
    queryset = SalaryAdavance.objects.filter(
        is_deleted=False, user__region=request.user.region
    ).order_by("-created")

    serializer = SalaryAdvanceListSerializer(
        queryset, context={"request": request}, many=True, read_only=True
    )
    response = {
        "status": 200,
        "data": serializer.data,
    }
    return Response(response, status=status.HTTP_200_OK)


   
