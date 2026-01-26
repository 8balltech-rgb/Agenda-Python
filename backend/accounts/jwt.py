# backend/accounts/jwt.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Le decimos a simplejwt qué campo esperamos (email)
    username_field = "email"

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise serializers.ValidationError("Email y password son requeridos.")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Credenciales inválidas.")

        if not user.check_password(password):
            raise serializers.ValidationError("Credenciales inválidas.")

        data = super().validate({self.username_field: email, "password": password})
        # info extra opcional
        data["user_type"] = getattr(user, "user_type", None)
        data["name"] = getattr(user, "full_name", "") or getattr(user, "team_name", "")
        return data


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
