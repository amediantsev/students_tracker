from datetime import datetime

from django.test import TestCase
from django.urls import reverse
from faker import Faker

from students.models import Student

fake = Faker()


class StudentListTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_students = 20
        for student_num in range(number_of_students):
            Student.objects.create(first_name=fake.first_name(),
                                   last_name=fake.last_name(),
                                   birth_date=datetime.now().date(),
                                   email=fake.email(),
                                   telephone=fake.phone_number(),
                                   address=fake.address(),
                                   )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/community/st_list/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('students'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('students'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'students_list.html')
