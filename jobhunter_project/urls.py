from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobhunter_app.urls')),  # Пустой путь будет направлять на URL из jobhunter_app.urls
]

