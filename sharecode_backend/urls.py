from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 将 /api/snippets/ 交给 snippets.urls 处理
    path('api/snippets/', include('snippets.urls')),
]
