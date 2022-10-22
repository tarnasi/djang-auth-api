from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import AppUserObtainPairSerializer


class AppUserObtainPairView(TokenObtainPairView):
    serializer_class = AppUserObtainPairSerializer
