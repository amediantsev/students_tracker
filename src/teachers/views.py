from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse

from teachers.forms import TeachersAddForm
from teachers.models import Teacher


def gen_teacher(request):
    response = Teacher.generate_teacher()
    return HttpResponse(response.get_info())


def teachers(request):
    queryset = Teacher.objects.all()

    fn_ln_email = request.GET.get('fn_ln_email')
    if fn_ln_email:
        queryset = queryset.filter(
            Q(first_name__contains=fn_ln_email) | Q(last_name__contains=fn_ln_email) | Q(email__contains=fn_ln_email))

    return render(request, 'teachers_list.html', context={'teachers_list': queryset})


def teachers_add(request):
    if request.method == 'POST':
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeachersAddForm()

    return render(request,
                  'teachers_add.html',
                  context={'form': form}
                  )


def teachers_edit(request, pk):
    try:
        teacher = Teacher.objects.get(id=pk)
    except Teacher.DoesNotExist:
        return HttpResponseNotFound(f'teacher with id {pk} not found')
    if request.method == 'POST':
        form = TeachersAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeachersAddForm(instance=teacher)

    return render(request,
                  'teachers_edit.html',
                  context={
                      'form': form,
                      'pk': pk,
                  }
                  )
