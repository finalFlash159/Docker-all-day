from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # Người dùng tạo công việc 
    title = models.CharField(max_length=255) # Tên công việc
    description = models.TextField(blank=True, null=True) # Mô tả
    completed = models.BooleanField(default=False) # Trạng thái công việc
    description = models.TextField(blank=True, null=True)  # Mô tả
    created_at = models.DateTimeField(auto_now_add=True) # Ngày tạo công việc

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['completed'] # Sắp xếp công việc theo trạng thái hoàn thành

        
