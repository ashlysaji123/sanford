from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.models import User


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @staticmethod
    def get_role(user):
        if user.is_superuser:
            role = "Superuser"
        elif user.is_merchandiser:
            role = "Merchandiser"
        elif user.is_sales_executive:
            role = "Sales_executive"
        elif user.is_sales_coordinator:
            role = "Sales_coordinator"
        elif user.is_sales_manager:
            role = "Sales_manager"
        return role

    @classmethod
    def get_token(cls, user):
        token = super(UserTokenObtainPairSerializer, cls).get_token(user)
        return token

    def validate(cls, attrs):
        data = super(UserTokenObtainPairSerializer, cls).validate(attrs)
        refresh = cls.get_token(cls.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["role"] = cls.get_role(cls.user)
        # data['demo'] = "demo"
        return data


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "first_name",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("old_password", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"}
            )
        return value

    def update(self, instance, validated_data):
        user = self.context["request"].user

        if user.pk != instance.pk:
            raise serializers.ValidationError(
                {"authorize": "You dont have permission for this user."}
            )

        instance.set_password(validated_data["password"])
        instance.save()

        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate_email(self, value):
        user = self.context["request"].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError(
                {"email": "This email is already in use."}
            )
        return value

    def validate_username(self, value):
        user = self.context["request"].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError(
                {"username": "This username is already in use."}
            )
        return value

    def update(self, instance, validated_data):
        user = self.context["request"].user

        if user.pk != instance.pk:
            raise serializers.ValidationError(
                {"authorize": "You dont have permission for this user."}
            )

        instance.first_name = validated_data["first_name"]
        instance.last_name = validated_data["last_name"]
        instance.email = validated_data["email"]
        instance.username = validated_data["username"]
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    fullname = serializers.ReadOnlyField()
    user_photo = serializers.ReadOnlyField(source="get_user_photo")
    average_points = serializers.ReadOnlyField(source="get_average_points.point__avg")
    total_points = serializers.ReadOnlyField(source="get_total_points.point__sum")

    class Meta:
        model = User
        fields = (
            "pk",
            "username",
            "fullname",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
            "user_photo",
            "average_points",
            "total_points",
            "is_merchandiser",
            "is_sales_manager",
            "is_sales_exicutive",
            "is_sales_coordinator",
        )
