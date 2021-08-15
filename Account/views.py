from .models import Account
from .serializers import RegisterSerializer, UserProfileSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class GetProfile(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

class ChangeProfile