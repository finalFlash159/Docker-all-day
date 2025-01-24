from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255) # Tên công việc
    completed = models.BooleanField(default=False) # Trạng thái công việc
    description = models.TextField(blank=True, null=True)  # Mô tả
    created_at = models.DateTimeField(auto_now_add=True) # Ngày tạo công việc

    def __str__(self):
        return self.title
