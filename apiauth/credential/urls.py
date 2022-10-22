from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import AppUserObtainPairView

app_name = 'credential'
urlpatterns = [
    path('admin/', admin.site.urls),

    # authentication
    path('login', AppUserObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
