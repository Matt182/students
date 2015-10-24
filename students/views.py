# -*- coding: utf-8 -*-

from django.contrib import auth
from django.shortcuts import render, redirect
from .models import GroupsSt, Students
from .forms import StudentsForm, GroupsForm
from django.template import RequestContext


def groups(request):
    """
    Представление для обработки событий на странице с группами
    """
    if auth.get_user(request).username:
        if auth.get_user(request).is_superuser:
            groupsList = GroupsSt.objects.all()
        else:
            groupsList = GroupsSt.objects.filter(author=auth.get_user(request))
        form = GroupsForm()
        context = RequestContext(request, {
            'username': auth.get_user(request).username,
            'groupsList': groupsList,
            'form': form,
        })

        if request.POST:
            if request.POST.get('action') == 'Delete':                       # В завимости какая конопка
                GroupsSt.objects.filter(id=request.POST.get('id')).delete()  # нажата (delete,update, add)
            elif request.POST.get('action') == 'Обновить':                   # выполняется соответсвующее
                new = GroupsSt.objects.get(id=request.POST.get('old'))       # действие
                if request.POST.get('newfaculty') != '':
                    new.faculty = request.POST.get('newfaculty')
                if request.POST.get('newname') != '':
                    new.name = request.POST.get('newname')
                if request.POST.get('newyear') != '':
                    new.created = request.POST.get('newyear')
                new.author = auth.get_user(request)
                new.save()
            else:
                GroupsSt.objects.create(faculty=request.POST.get('faculty'), name=request.POST.get('name'),
                                        created=request.POST.get('year'), author=auth.get_user(request))
        return render(request, 'students/groups.html', context)
    else:
        return redirect('/')


def students(request):
    """
    Представление для обработке событий на странице со студентами
    """
    if auth.get_user(request).username:
        if auth.get_user(request).username == 'admin':
            studentsList = Students.objects.all()
        else:
            studentsList = Students.objects.filter(author=auth.get_user(request))
        form = StudentsForm()
        context = RequestContext(request, {
            'username': auth.get_user(request).username,
            'studentsList': studentsList,
            'form': form,
        })
        if request.POST:
            if request.POST.get('action') == 'Delete':
                Students.objects.filter(id=request.POST.get('id')).delete()
            elif request.POST.get('action') == 'Обновить':
                new = Students.objects.get(id=request.POST.get('old'))
                if request.POST.get('group') != '':
                    new.group = request.POST.get('group')
                if request.POST.get('first_name') != '':
                    new.first_name = request.POST.get('first_name')
                if request.POST.get('second_name') != '':
                    new.second_name = request.POST.get('second_name')
                new.author = auth.get_user(request)
                new.save()
            else:
                Students.objects.create(group_id=request.POST.get('group'), first_name=request.POST.get('first_name'),
                                        second_name=request.POST.get('second_name'), author=auth.get_user(request))

        return render(request, 'students/students.html', context)
    else:
        return redirect('/')


