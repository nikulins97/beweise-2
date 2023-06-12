from django.contrib import admin
from django.urls import path

from app.views import NumberAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('number/', NumberAPIView.as_view()),
]
