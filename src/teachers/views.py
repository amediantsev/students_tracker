from django.http import HttpResponse
from django.shortcuts import render
from teachers.models import Teacher
from django.db.models import Q


def gen_teacher(request):
    response = Teacher.generate_teacher()
    return HttpResponse(response.get_info())

def teachers(request):
    queryset = Teacher.objects.all()
    response = ''

    fn_ln_email = request.GET.get('fn_ln_email')
    if fn_ln_email:
        queryset = queryset.filter(Q(first_name__contains=fn_ln_email) | Q(last_name__contains=fn_ln_email) | Q(email__contains=fn_ln_email))
        print(queryset.query)

    for teacher in queryset:
        response += teacher.get_info() + '<br>'
    return render(request, 'teachers_list.html', context={'teachers_list' : response})
