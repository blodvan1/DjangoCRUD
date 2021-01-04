from django.db import models
from django.db.models import Max

# Create your models here.
class Employee(models.Model):

	emp_no = models.IntegerField(primary_key=True)
	sesa_id = models.CharField(max_length=255)
	first_name = models.CharField(max_length=14)
	last_name = models.CharField(max_length=16)
	gender = models.CharField(max_length=1)

def generate_next_emp_no():
	return 1 if Employee.objects.all().count() == 0 else Employee.objects.all().aggregate(Max('emp_no'))['emp_no__max'] + 1
