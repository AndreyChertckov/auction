"""
Views for the user model
"""

from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.serilizers import UserSerializer

User = get_user_model()


class UserCreate(generics.CreateAPIView):
    """
    Register/Create view
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
