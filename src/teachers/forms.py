from django.forms import ModelForm, ValidationError

from teachers.models import Teacher


class TeachersAddForm(ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'

    def clean_email(self):
        email = self.email
        email_exists = Teacher.objects. \
            filter(email__iexact=email). \
            exclude(email__iexact=self.instance.email) \
            .exists()
        if email_exists:
            raise ValidationError(f'{email} is already used!')
        return email


class TeacherAdminForm(TeachersAddForm):
    pass
