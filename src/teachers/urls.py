from django.urls import path

from teachers.views import *


urlpatterns = [
    path('gen/', gen_teacher, name='gen-teacher'),
    path('list/', teachers, name='teachers'),
    path('add/', teachers_add, name='teachers-add'),
    path('edit/<int:pk>/', teachers_edit, name='teachers-edit'),
]
