from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy # Để redirect sau khi tạo todo


from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin 


from .models import Todo


class CustomLoginView(LoginView):
    template_name = 'todos/login.html'
    fields = '__all__'
    redirect_authenticated_user = True # Nếu người dùng đã đăng nhập thì sẽ redirect về trang chính

    def get_success_url(self):
        return reverse_lazy('todo_list')

 
class TodoListView(LoginRequiredMixin, ListView): # LoginRquiredMixin để kiểm tra người dùng đã đăng nhập hay chưa
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos' # Tên biến sẽ được truyền vào template

    def get_context_data(self, **kwargs): # **kwargs: nhận các tham số truyền vào dưới dạng từ điển
        context = super().get_context_data(**kwargs) # Lấy context mặc định
        context['todos'] = context['todos'].filter(user=self.request.user) # Lọc công việc theo người dùng
        context['count'] = context['todos'].filter(completed=False).count() # Đếm số công việc chưa hoàn thành
        return context



class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todos/todo.html'
    context_object_name = 'todo' # Tên biến sẽ được truyền vào template

class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'completed'] # Các field cần tạo
    success_url = reverse_lazy('todo_list') # Redirect sau khi tạo todo
    template_name = 'todos/task_form.html'

    def form_invalid(self, form):
        form.instance.user = self.request.user # Gán người dùng hiện tại vào trường user
        return super(TodoCreate, self).form_valid(form) # Gọi phương thức form_valid của class cha để lưu todo

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'description', 'completed'] # Các field cần tạo
    template_name = 'todos/task_form.html'
    success_url = reverse_lazy('todo_list') # Redirect sau khi update todo

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todos/task_confirm_delete.html'
    success_url = reverse_lazy('todo_list') # Redirect sau khi xóa todo
    context_object_name = 'todo'