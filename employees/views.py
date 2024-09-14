from django.shortcuts import render
from .models import Employee
from django.core.paginator import Paginator
from .forms import EmployeeForm
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q

def home(request):
    # Home page view
    return render(request, 'home.html')

def employee_list(request):
    # Get search query values from GET request
    name = request.GET.get('name', '')
    email = request.GET.get('email', '')
    dob = request.GET.get('dob', '')
    mobile = request.GET.get('mobile', '')
    sort_by = request.GET.get('sort_by', None)  # No default sorting

    # Build the query dynamically using Q objects
    query = Q()

    if name:
        query &= Q(first_name__icontains=name) | Q(last_name__icontains=name)
    if email:
        query &= Q(email__icontains=email)
    if dob:
        query &= Q(dob=dob)  # Exact match for date of birth
    if mobile:
        query &= Q(mobile=mobile)  # Exact match for mobile number

    # Sort employees if a sorting column is selected
    if sort_by:
        employees = Employee.objects.filter(query).order_by(sort_by)
    else:
        employees = Employee.objects.filter(query).order_by('id')  # Default order of adding employees is employee id

    # Pagination
    paginator = Paginator(employees, 10)
    page = request.GET.get('page')
    employees_page = paginator.get_page(page)

    # Check if no employees were found
    no_employee_found = not employees.exists()

    return render(request, 'employee_list.html', {
        'employees': employees_page,
        'no_employee_found': no_employee_found,
        'name': name,
        'email': email,
        'dob': dob,
        'mobile': mobile,
        'sort_by': sort_by,  # Pass the sort_by value to the template
    })



def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})



def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})



def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

