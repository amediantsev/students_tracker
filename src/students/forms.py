from datetime import datetime

from django.forms import ModelForm, Form,\
    EmailField, CharField, ValidationError
from django.core.mail import send_mail
from django.conf import settings

from students.models import Student, Group


class StudentsAddForm(ModelForm):

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
            raise ValidationError(f'{email} is already used!')
        return email


class StudentAdminForm(StudentsAddForm):
    pass


class ContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data

        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, email_from, recipient_list)
        with open('emails_logs.txt', 'a') as file:
            file.write(str(datetime.now()) +
                       '\nFrom: ' + email_from +
                       '\nRecipients: ' + '; '.join(recipient_list) +
                       '\nSubject: ' + subject +
                       '\nMessages text: ' + message + '\n' + '\n'
                       )


class GroupsAddForm(ModelForm):

    class Meta:
        model = Group
        fields = '__all__'
