from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def index(request):
    form = TodoForm()
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'index.html', {'form': form, 'todos': todos})



def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'update.html', {'form': form})



def delete(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect('index')