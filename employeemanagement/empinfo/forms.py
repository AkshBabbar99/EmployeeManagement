from django import forms
from .models import Department

class DepartmentForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=True,
        label='Department Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )

    def __init__(self, *args, **kwargs):
        department = kwargs.pop('instance', None)
        super(DepartmentForm, self).__init__(*args, **kwargs)
        if department is not None:
            self.fields['name'].initial = department.name
            self.fields['description'].initial = department.description


class EmployeeForm(forms.Form):
    employee_id = forms.IntegerField(required=False, label='Employee ID')
    first_name = forms.CharField(max_length=50, required=True, label='First Name')
    last_name = forms.CharField(max_length=50, required=True, label='Last Name')
    email = forms.EmailField(required=True, label='Email')
    date_of_birth = forms.DateField(required=True, label='Date of Birth')
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=True, label='Department')
    job_title = forms.CharField(max_length=100, required=True, label='Job Title')
    salary = forms.DecimalField(max_digits=10, decimal_places=2, required=True, label='Salary')

    def __init__(self, *args, **kwargs):
        employee = kwargs.pop('instance', None)
        super(EmployeeForm, self).__init__(*args, **kwargs)
        if employee is not None:
            self.fields['employee_id'].initial = employee.employee_id
            self.fields['first_name'].initial = employee.first_name
            self.fields['last_name'].initial = employee.last_name
            self.fields['email'].initial = employee.email
            self.fields['date_of_birth'].initial = employee.date_of_birth
            self.fields['department'].initial = employee.department
            self.fields['job_title'].initial = employee.job_title
            self.fields['salary'].initial = employee.salary