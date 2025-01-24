from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list, name="todo_list"),  # Đường dẫn gốc cho danh sách todos
    path("add/", views.add_todo, name="add_todo"),  # Đường dẫn thêm mới todos
]