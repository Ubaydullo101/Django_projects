from django.shortcuts import render
from .models import To_Do_Task
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class Task_View(ListView):
    model = To_Do_Task
    template_name = 'index.html'

class Create_Task(CreateView):
    model = To_Do_Task
    template_name = 'new_task.html'
    fields = '__all__'
    success_url = reverse_lazy('home_page')

class Task_Update_View(UpdateView):
    model = To_Do_Task
    template_name = 'update_task.html'
    fields = ['task']
    success_url = reverse_lazy('home_page')

class Delete_Task(DeleteView):
    model = To_Do_Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('home_page')

def task_detail(request,id):
    task=To_Do_Task.objects.get(id=id)
    return render(request=request,
                  template_name='task_detatil.html',
                  context={
                      'task':task
                  })