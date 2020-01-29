from django.contrib import admin
from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ('email', )
    list_display = ('id', 'first_name', 'last_name', 'academic_degree', 'email')
    list_per_page = 20

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)

        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('telephone', )
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Teacher, TeacherAdmin)
