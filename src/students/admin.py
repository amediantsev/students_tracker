from django.contrib import admin

from students.models import Student, Group
from students.forms import StudentAdminForm


class StudentAdmin(admin.ModelAdmin):
    # readonly_fields = ('email', )
    list_display = ('id', 'first_name', 'last_name', 'email', 'birth_date', 'telephone', 'address', 'group')
    list_select_related = ('group',)
    list_per_page = 40
    form = StudentAdminForm

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)

        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('telephone', )
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False


class StudentInline(admin.TabularInline):
    model = Student


class GroupAdmin(admin.ModelAdmin):
    # readonly_fields = ('email', )
    list_display = ('id', 'name', 'specialization', 'headman', 'curator')
    list_select_related = ('headman', 'curator')
    list_per_page = 20
    inlines = [
        StudentInline,
    ]

    # def get_readonly_fields(self, request, obj=None):
    #     readonly_fields = super().get_readonly_fields(request, obj)

        # if request.user.groups.filter(name='manager').exists():
        #     return readonly_fields + ('telephone', )
        # return readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
