# -*- coding: utf-8 -*-

from django.forms import ModelForm
from .models import Students, GroupsSt


class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['group', 'first_name', 'second_name']
        labels = {
            'group': 'Группа',
            'first_name': 'Имя',
            'second_name': 'Фамилия'
        }


class GroupsForm(ModelForm):

    class Meta:
        model = GroupsSt
        fields = ['faculty', 'name']
        labels = {
            'faculty': 'Факультет',
            'name': 'Группа',
        }
