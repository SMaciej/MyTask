from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response
from .models import Task
from django.shortcuts import redirect
from .forms import AddTaskForm
import slumber

def home(request):

    current_user = request.user

    user_tasks = Task.objects.filter(owner=current_user.id)

    if request.GET.get('clear'):
        clear(current_user)
        return redirect('/')

    elif request.POST.get('check'):
        check(request.POST.get('check'), current_user)
        return redirect('/')

    task_form = AddTaskForm(request.POST or None)
    if task_form.is_valid():
        new_task = task_form.save(commit=False)
        new_task.owner = current_user
        new_task.save()
        return redirect('/')

    template = 'base.html'
    context = {'current_user':current_user, 'user_tasks':user_tasks, 'task_form':task_form}

    return render_to_response(template, context, context_instance=RequestContext(request))


def clear(current_user):
    """ Usuwa z bazy danych wykonane zadania. """

    for task in Task.objects.filter(owner=current_user.id):
        if task.status == True:
            task.delete()


def check(task_id, current_user):
    """ Zaznacza lub odznacza zadanie. """

    print "WYKONUJE CHECK"

    for task in Task.objects.filter(owner=current_user.id):
        if task.id == int(task_id):
            new_task = Task.objects.get(id=task.id)
            new_task.status = not task.status
            new_task.save()