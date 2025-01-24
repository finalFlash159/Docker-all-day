from django.shortcuts import render, redirect

from .models import Todo

# Hiển thị danh sách todo
def todo_list(request):
    todos = Todo.objects.all() # Lấy tất cả các todo từ database
    return (render(request, "todos/todo_list.html", {"todos": todos}))

# Thêm mới todo
def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title") # Lấy dữ liệu từ form
        description = request.POST.get("description")
        todo = Todo(title=title, description=description) # Tạo một todo mới
        todo.save() # Lưu todo mới vào database
        return redirect("todos:todo_list") # Chuyển hướng về trang danh sách todo
    return render(request, "todos/add_todo.html")