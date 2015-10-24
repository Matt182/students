from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logout/', views.logout, name='Logout'),
    url(r'^register/', views.register, name='Register'),
    url(r'^$', views.login, name='Login'),

]
