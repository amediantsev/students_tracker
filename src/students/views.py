from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from students.models import Student, Group
from students.forms import StudentsAddForm, ContactForm, GroupsAddForm
from django.urls import reverse


def gen_stud(request):
    response = Student.generate_student()
    return HttpResponse(response.get_info())


def students(request):
    queryset = Student.objects.all()

    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__contains=fn)

    return render(request,
                  'students_list.html',
                  context={'students_list': queryset}
                  )


def gen_group(request):
    response = Group.generate_group()
    return HttpResponse(response.get_info())


def groups(request):
    queryset = Group.objects.all()

    specials = request.GET.get('specialization')
    if specials:
        queryset = queryset.filter(specialization__contains=specials)

    return render(request,
                  'groups_list.html',
                  context={'groups_list': queryset}
                  )


def groups_add(request):
    if request.method == 'POST':
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm()

    return render(request,
                  'groups_add.html',
                  context={'form': form}
                  )


def students_add(request):
    if request.method == 'POST':
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm()

    return render(request,
                  'students_add.html',
                  context={'form': form}
                  )


def students_edit(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound(f'Student with id {pk} not found')
    if request.method == 'POST':
        form = StudentsAddForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm(instance=student)

    return render(request,
                  'students_edit.html',
                  context={
                      'form': form,
                      'pk': pk,
                  }
                  )


def groups_edit(request, pk):
    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return HttpResponseNotFound(f'Group with id {pk} not found')
    if request.method == 'POST':
        form = GroupsAddForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm(instance=group)

    return render(request,
                  'groups_edit.html',
                  context={
                      'form': form,
                      'pk': pk
                  }
                  )


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = ContactForm()

    return render(request,
                  'contact.html',
                  context={'form': form}
                  )
