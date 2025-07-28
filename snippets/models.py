# snippets/models.py
from django.db import models
import uuid

class Snippet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.TextField()
    language = models.CharField(max_length=50, default='html')
    theme = models.CharField(max_length=50, default='light')  # 'light' or 'dark'
    created = models.DateTimeField(auto_now_add=True)

    # ✅ 新增收藏字段，默认不收藏
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.language} snippet created on {self.created}"
