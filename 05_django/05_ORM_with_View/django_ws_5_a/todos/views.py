from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, work):
    todo = Todo.objects.get(work=work)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)