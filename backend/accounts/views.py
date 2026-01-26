from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Usuario creado correctamente"},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "email": request.user.email,
            "user_type": request.user.user_type,
            "name": request.user.full_name or request.user.team_name,
        })
