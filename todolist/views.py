from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import ToDo

# Create your views here.
def index(request):
    todos = ToDo.objects.all()
    context = {
        'todo_list': todos,
        'title': 'Главная страница'
    }
    return render(request, 'todoapp/index.html', context)

def add(request):
    if request.method == 'GET':
        return render(request, 'todoapp/addToDo.html')

    elif request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        ToDo.objects.create(title=title, description=description)
        return redirect('index')

def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

def edit(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    if request.method == 'POST':
       todo.title = request.POST['title']
       todo.description = request.POST['description']
       todo.save()
       return redirect('index')
    else:
        return render(request, 'todoapp/editToDo.html', {'todo': todo})

def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')

