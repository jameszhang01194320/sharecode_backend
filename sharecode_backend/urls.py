# sharecode_backend/urls.py
from django.contrib import admin  # ✅ 加上这一行
from django.http import HttpResponse
from django.urls import path, include

def home(request):
    return HttpResponse("Welcome to ShareCode Backend API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/snippets/', include('snippets.urls')),
    path('', home),  # 添加这一行
]
