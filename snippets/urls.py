# snippets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 对应你在 views.py 里写的 APIView 或 ViewSet
    path('', views.SnippetListCreate.as_view(), name='snippet-list-create'),
    path('<uuid:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
]
