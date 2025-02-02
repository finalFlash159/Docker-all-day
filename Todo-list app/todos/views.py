from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy # Để redirect sau khi t ạo todo
from .models import Todo

 
class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos' # Tên biến sẽ được truyền vào template


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todos/todo.html'
    context_object_name = 'todo' # Tên biến sẽ được truyền vào template

class TodoCreate(CreateView):
    model = Todo
    fields = '__all__' # Tạo form từ tất cả các field trong model
    success_url = reverse_lazy('todo_list') # Redirect sau khi tạo todo
    template_name = 'todos/task_form.html'

class TaskUpdate(UpdateView):
    model = Todo
    fields = '__all__' # Các field cần update
    template_name = 'todos/task_form.html'
    success_url = reverse_lazy('todo_list') # Redirect sau khi update todo

class TaskDelete(DeleteView):
    model = Todo
    template_name = 'todos/task_confirm_delete.html'
    success_url = reverse_lazy('todo_list') # Redirect sau khi xóa todo
    context_object_name = 'todo'