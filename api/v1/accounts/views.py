from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.models import User

from .serializers import (
    ChangePasswordSerializer,
    UpdateUserSerializer,
    UserSerializer,
    UserTokenObtainPairSerializer,
)


class MyObtainTokenPairView(TokenObtainPairView):
    """
    View to generate access and refresh token with username and password
    """

    permission_classes = (AllowAny,)
    serializer_class = UserTokenObtainPairSerializer


class ChangePasswordView(UpdateAPIView):
    """
    View to change password of a user (pk in the url identifies the user)
    """

    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]


class UpdateProfileView(UpdateAPIView):
    """
    View to change password of a user (pk in the url identifies the user)
    """

    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated]


class MyProfileView(APIView):
    """
    View to get all information associated with current user
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UserProfileView(RetrieveAPIView):
    """
    View to get all information associated with user identified by pk
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
