from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from todolist.forms import ToDoForm, OrderForm

from .models import ToDo

# Create your views here.
def index(request):
    todos = ToDo.objects.all()
    order_form = OrderForm(request.GET)
    if order_form.is_valid():
        todos = todos.order_by(order_form.cleaned_data['order_by'])
    context = {
        'todo_list': todos,
        'title': 'Главная страница'
    }
    return render(request, 'todoapp/index.html', context)

def add(request):
    form = ToDoForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'todoapp/addToDO.html', context={'form': form})

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

