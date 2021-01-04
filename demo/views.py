from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views import generic
from .models import Employee, generate_next_emp_no
from .forms import ( EmployeeForm,) 

# Create your views here.
class EmployeeListView(generic.ListView):
    model = Employee
    template_name = 'demo/employee.html'
    paginate_by = 100

    def get_queryset(self):
        queryset = super(EmployeeListView, self).get_queryset()
        return queryset

class EmployeeCreateView(generic.CreateView):
    template_name = 'demo/employee_create.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee')

    def get_initial(self):
        initial = super(EmployeeCreateView, self).get_initial()
        initial['emp_no'] = generate_next_emp_no()
        return initial

class EmployeeDeleteView(generic.DeleteView):
    model = Employee
    success_url = reverse_lazy('employee')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class EmployeeUpdateView(generic.UpdateView):
    template_name = 'demo/employee_update.html'
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employee')

class IndexGenericView(generic.TemplateView):
    template_name = 'demo/main.html'