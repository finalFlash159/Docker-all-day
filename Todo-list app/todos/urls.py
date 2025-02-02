from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"), # Đường dẫn đến trang đăng nhập
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"), # Đường dẫn đến trang đăng xuất
    path("register/", RegisterPage.as_view(), name="register"), # Đường dẫn đến trang đăng ký
    path("", TodoListView.as_view(), name="todo_list"), # Đường dẫn đến trang danh sách công việc
    path("task/<int:pk>/", TodoDetailView.as_view(), name="todo_detail"), # Đường dẫn đến trang chi tiết công việc
    path("task-create/", TodoCreate.as_view(), name="task-create"), 
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="task-delete"), 

]