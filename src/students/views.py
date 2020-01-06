from django.http import HttpResponse
from django.shortcuts import render
from students.models import Student, Group
from django.db.models import Q


def gen_stud(request):
    response = Student.generate_student()
    return HttpResponse(response.get_info())

def students(request):
    queryset = Student.objects.all()
    response = ''

    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__contains=fn)
        print(queryset.query)
    for student in queryset:
        response += student.get_info() + '<br>'
    return render(request, 'students_list.html', context={'students_list' : response})

def gen_group(request):
    response = Group.generate_group()
    return HttpResponse(response.get_info())

def groups(request):
    queryset = Group.objects.all()
    response = ''

    specials = request.GET.get('specialization')
    if specials:
        queryset = queryset.filter(specialization__contains=specials)
        print(queryset.query)

    for group in queryset:
        response += group.get_info() + '<br>'
    return render(request, 'groups_list.html', context={'groups_list' : response})
