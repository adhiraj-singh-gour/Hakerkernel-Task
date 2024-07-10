from django.urls import path
from.views import *

urlpatterns = [
    path('',user, name='user'),
    path('tasks/',tasks, name='tasks'),
    path('UserList/',UserList, name='UserList'),
    path('TaskList/',TaskList, name='TaskList'),
    path('Task_into_excell/',Task_into_excell, name='Task_into_excell'),
    path('User_to_excel/',User_to_excel, name='User_to_excel'),


]