from datetime import datetime

from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command
from faker import Faker

from students.models import Student

#
# class StudentListTestCase(TestCase):
#     fake = Faker()
#
#     @classmethod
#     def setUpTestData(cls):
#         number_of_students = 20
#         for student_num in range(number_of_students):
#             Student.objects.create(first_name=fake.first_name(),
#                                    last_name=fake.last_name(),
#                                    birth_date=datetime.now().date(),
#                                    email=fake.email(),
#                                    telephone=fake.phone_number(),
#                                    address=fake.address(),
#                                    )
#
#     def test_view_students_list(self):
#         resp = self.client.get(reverse('students'))
#         self.assertEqual(resp.status_code, 200)



#
# class StudentEditTestCase(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         number_of_students = 20
#         for student_num in range(number_of_students):
#             Student.objects.create(first_name=fake.first_name(),
#                                    last_name=fake.last_name(),
#                                    birth_date=datetime.now().date(),
#                                    email=fake.email(),
#                                    telephone=fake.phone_number(),
#                                    address=fake.address(),
#                                    )
#
#     def test_view_students_edit(self):
#         resp = self.client.post(reverse('students-edit'))
#         self.assertEqual(resp.status_code, 200)

#     def test_view_url_accessible_by_name(self):
#         resp = self.client.post(reverse('students-edit'))
#         self.assertEqual(resp.status_code, 200)
#
#     # def test_view_uses_correct_template(self):
#     #     resp = self.client.get(reverse('students'))
#     #     self.assertEqual(resp.status_code, 200)
#     #
#     #     self.assertTemplateUsed(resp, 'students_list.html')



# class TestContact(TestCase):
#
#     def test_contact_is_valid(self):
#         assert False

class TestStudent(TestCase):
    fake = Faker()

    @classmethod
    def setUpClass(cls):
        call_command('loaddata', 'db.json', verbosity=0)


    def _gen_data(self):
        return {
            'subject': self.fake.word(),
            'text': self.fake.text(),
        }

    def test_contact_form(self):
        data = {
            'email': self.fake.email(),
            **self._gen_data(),
        }
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 302

    def test_contact_form_wrong_email(self):
        data = {
            'email': 'wrong_email',
            **self._gen_data(),
        }
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 200

    def test_contact_form_empty_subject(self):
        data = {
            'email': self.fake.email(),
            'subject': '',
            'text': self.fake.text(),
        }
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 200
