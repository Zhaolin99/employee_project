from django.core.management.base import BaseCommand
from employees.models import Employee, Department
from faker import Faker
import random

class Command(BaseCommand):
    help = "Seed the database with fake employees"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create departments if none exist
        departments = ['HR', 'Engineering', 'Marketing', 'Sales']
        for name in departments:
            Department.objects.get_or_create(name=name)

        department_objs = list(Department.objects.all())

        for _ in range(50):
            Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                date_joined=fake.date_between(start_date='-2y', end_date='today'),
                department=random.choice(department_objs)
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded 50 employees.'))
