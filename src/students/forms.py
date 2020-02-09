from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings

from students.models import Student, Group
from students.tasks import send_email_async


class StudentsAddForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        list_select_related = ['curator', ]

    def clean_email(self):
        email = self.instance.email
        email_exists = Student.objects. \
            filter(email__iexact=email). \
            exclude(email__iexact=self.instance.email) \
            .exists()
        if email_exists:
            raise forms.ValidationError(f'{email} is already used!')
        return email


# class RegForm(UserCreationForm):
#     email = forms.EmailField(max_length=200)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#
#     def save(self):
#         data = self.cleaned_data
#         subject = 'Confirmation of registration'
#         message = 'Hello, buddy'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [data['email']]
#         send_email_async.delay(subject, message, email_from, recipient_list)
#         super(RegForm, self).save(self)


class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.set_password(self.cleaned_data)
        super().save(commit)


class UserLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()


class StudentAdminForm(StudentsAddForm):
    pass


class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    text = forms.CharField()

    def save(self):
        data = self.cleaned_data

        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER]
        send_email_async.delay(subject, message, email_from, recipient_list)
        with open('emails_logs.txt', 'a') as file:
            file.write(str(datetime.now()) +
                       '\nFrom: ' + email_from +
                       '\nRecipients: ' + '; '.join(recipient_list) +
                       '\nSubject: ' + subject +
                       '\nMessages text: ' + message + '\n' + '\n'
                       )


class GroupsAddForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'
