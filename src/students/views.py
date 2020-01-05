from django.http import HttpResponse
from django.shortcuts import render
from students.models import Student

# Create your views here.
def gen_stud(request):
    response = Student.generate_student()
    return HttpResponse(response.get_info())

def students(request):
    queryset = Student.objects.all()
    response = ''

    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__startswith=fn)
        print(queryset.query)
    for student in queryset:
        response += student.get_info() + '<br>'
    return render(request, 'students_list.html', context={'students_list' : response})
