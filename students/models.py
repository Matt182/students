from django.db import models
from django.contrib.auth.models import User


class GroupsSt(models.Model):
    faculty = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    created = models.DateField('date created')
    author = models.ForeignKey(User)

    def __str__(self):
        return self.faculty + ' ' + self.name + ' ' + str(self.created)


class Students(models.Model):
    group = models.ForeignKey(GroupsSt)
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    author = models.ForeignKey(User)

    def __str__(self):
        return str(self.group) + ' ' + self.first_name + ' ' + self.second_name


