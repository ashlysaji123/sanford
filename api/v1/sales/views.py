import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sales.models import Sales

from .serializers import CreateSalesSerializer, SalesSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_sales(request):
    serializer = CreateSalesSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        serializer.save(user=request.user, creator=request.user)
        response = {"message": "Successfully Submitted."}
        return Response(response, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_sale(request, pk):
    instance = Sales.objects.get(pk=pk)
    serializer = CreateSalesSerializer(
        instance, data=request.data, context={"request": request}
    )
    if serializer.is_valid():
        serializer.save(updater=request.user)
        response = {"message": "Successfully Updated."}
        return Response(response, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_sales(request):
    current_month = datetime.datetime.now().month
    queryset = Sales.objects.filter(
        is_deleted=False, user=request.user, created__month=current_month
    ).order_by("-created")

    serializer = SalesSerializer(
        queryset, context={"request": request}, many=True, read_only=True
    )

    return Response(serializer.data, status=status.HTTP_200_OK)


# class MyTarget(APIView):
#     """
#     Returns Target assigned with curent user in the current year and month, returns false if no target assigned
#     """
#     queryset=Target.objects.filter(is_deleted=False),
#     serializer_class=TargetSerializer,
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         try:
#             current_year = datetime.datetime.now().year
#             current_month = datetime.datetime.now().month
#             target = Target.objects.get(user=request.user,year=current_year, month=current_month)
#             response_data = {
#                 "status" : True,
#                 "target" : str(target.amount),
#             }
#         except Target.DoesNotExist:
#             target = None
#             response_data = {
#                 "status" : False,
#                 "detail" : "No Target Assigned",
#             }
#         return Response(response_data)
