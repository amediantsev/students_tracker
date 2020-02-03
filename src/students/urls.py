from django.urls import path

from students.views import *


urlpatterns = [
    path('st_gen/', gen_stud, name='gen-stud'),
    path('st_list/', students, name='students'),
    path('st_add/', students_add, name='students-add'),
    path('gr_list/', groups, name='groups'),
    path('gr_add/', groups_add, name='groups-add'),
    path('gr_gen/', gen_group, name='gen-group'),
    path('gr_edit/<int:pk>/', groups_edit, name='groups-edit'),
    path('st_edit/<int:pk>/', students_edit, name='students-edit'),
    path('contact/', contact, name='contact'),
    path('reg/', Registration.as_view(), name='students-reg'),
]
