from django.shortcuts import render
from django.http import JsonResponse
from .models import Todo

def todo_list(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            todo = Todo.objects.create(title=title)
            return JsonResponse({'id': todo.id, 'title': todo.title})
        return JsonResponse({'error': 'Title is required'}, status=400)

    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})
