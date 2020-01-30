from django.contrib import admin

from teachers.models import Teacher
from teachers.forms import TeacherAdminForm


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = []
    list_display = ('id', 'first_name', 'last_name', 'academic_degree', 'email', 'telephone')
    list_per_page = 20
    form = TeacherAdminForm

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)

        if request.user.groups.filter(name='manager').exists():
            readonly_fields.append('email', 'telephone')
            return readonly_fields
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Teacher, TeacherAdmin)
