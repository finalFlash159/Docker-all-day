from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"), # Đường dẫn đến trang danh sách công việc
    path("task/<int:pk>/", TodoDetailView.as_view(), name="todo_detail"), # Đường dẫn đến trang chi tiết công việc
    path("task-create/", TodoCreate.as_view(), name="task-create"), 
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="task-delete"), 

]