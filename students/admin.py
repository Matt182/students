from django.contrib import admin
from .models import GroupsSt, Students


class GroupsAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'name', 'created')


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('group', 'first_name', 'second_name')

admin.site.register(GroupsSt, GroupsAdmin)
admin.site.register(Students, StudentsAdmin)
