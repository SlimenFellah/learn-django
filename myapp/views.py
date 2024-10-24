from django.shortcuts import render
from django.http import HttpResponse
from .models import toDoList

# Create your views here.
def home(request):
    # return HttpResponse('Hello, World!')
    return render(request, 'home.html')

def todo_list(request):
    items = toDoList.objects.all()
    return render(request, 'todos.html', {'todos': items})