from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Department, Employee
from .forms import DepartmentForm, EmployeeForm
from django.contrib import messages

# Create your views here.

def index(response):
    return render(response, 'empinfo/index.html', {})

def departments(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'empinfo/departments.html', context)

def department_detail(request, id):
    department = Department.objects.get(id=id)
    employees = Employee.objects.filter(department=department)
    context = {'department': department, 'employees': employees}
    return render(request, 'empinfo/department_details.html', context)

def add_department(request):
    form = DepartmentForm()
    context = {'form': form}
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            if Department.objects.filter(name=name).exists():
                context['error_message'] = 'Error: A department with the same name already exists'
            else:
                d = Department(name=name, description=description)
                d.save()
                messages.success(request, 'Form submitted successfully')
                return redirect('department_detail', id=d.id)
    return render(request, 'empinfo/add_department.html', context)

def delete_department(request, id):
    department = Department.objects.get(id=id)
    if request.method == 'POST':
        department.delete()
        return redirect('departments')
    return render(request, 'empinfo/delete_department.html', {'department': department})

def edit_department(request, id):
    department = Department.objects.get(id=id)
    form = DepartmentForm(instance=department)
    context = {'form': form, 'department': department}
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            if name == department.name and description == department.description:
                context['error_message'] = 'Error: No changes were made'
            else:
                # Check if the new department name already exists in the database
                existing_department = Department.objects.filter(name=name).exists()
                if existing_department and name != department.name:
                    context['error_message'] = 'Error: A department with the same name already exists'
                else:
                    department.name = name
                    department.description = description
                    department.save()
                    return redirect('department_detail', id=department.id)
    return render(request, 'empinfo/edit_department.html', context)

def employees(request):
    employees = Employee.objects.all().order_by('first_name')
    context = {'employees': employees}
    return render(request, 'empinfo/employees.html', context)

def employee_detail(request, id):
    employee = Employee.objects.get(employee_id=id)
    context = {'employee': employee}
    return render(request, 'empinfo/employee_details.html', context)

def edit_employee(request, id):
    employee = get_object_or_404(Employee, employee_id=id)
    form = EmployeeForm(instance=employee)
    form.fields['employee_id'].disabled = True
    # form.fields['employee_id'] = False
    context = {'form': form, 'employee': employee}

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date_of_birth = form.cleaned_data['date_of_birth']
            department = form.cleaned_data['department']
            job_title = form.cleaned_data['job_title']
            salary = form.cleaned_data['salary']
            if first_name == employee.first_name and last_name == employee.last_name and email == employee.email and date_of_birth == employee.date_of_birth and department == employee.department and job_title == employee.job_title and salary == employee.salary:
                context['error_message'] = 'Error: No changes were made'
            else:
                employee.employee_id = id
                employee.first_name = first_name
                employee.last_name = last_name
                employee.email = email
                employee.date_of_birth = date_of_birth
                employee.department = department
                employee.job_title = job_title
                employee.salary = salary
                employee.save()
                return redirect('employee_detail', id=employee.employee_id)
        else:
            print(form.errors)
    return render(request, 'empinfo/edit_employee.html', context)

def delete_employee(request, id):
    employee = get_object_or_404(Employee, employee_id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees')
    return render(request, 'empinfo/delete_employee.html', {'employee': employee})

def add_employee(request):
    form = EmployeeForm()
    context = {'form': form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            employee_id = int(form.cleaned_data['employee_id'])
            if Employee.objects.filter(email=email).exists():
                context['error_message'] = 'An employee with this email address already exists.'
            elif Employee.objects.filter(employee_id=employee_id).exists():
                context['error_message'] = 'An employee with this ID already exists.'
            else:
                # Save the form data to the database
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                date_of_birth = form.cleaned_data['date_of_birth']
                department = form.cleaned_data['department']
                job_title = form.cleaned_data['job_title']
                salary = form.cleaned_data['salary']

                employee = Employee(
                    first_name=first_name, 
                    last_name=last_name, 
                    email=email, 
                    employee_id=employee_id, 
                    date_of_birth=date_of_birth, 
                    department=department, 
                    job_title=job_title, 
                    salary=salary
                )
                employee.save()
                return redirect('employee_detail', id=employee.employee_id)
        else:
            print(form.errors)
    return render(request, 'empinfo/add_employee.html', context)



