from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # authentication
    path('api/v1/', include('credential.urls', namespace='credential'))
]
