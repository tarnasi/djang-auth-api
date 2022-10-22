from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AppUserObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['is_admin'] = user.is_admin
        token['is_active'] = user.is_active

        return token
