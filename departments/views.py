# # from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from .models import Department
# from .forms import DepartmentForm

# # List all departments
# # def department_list(request):
# #     departments = Department.objects.all()
# #     print("Departments:", departments) 
# #     return render(request, 'departments/department_list.html', {'departments': departments})

# def department_list(request):
#     departments = Department.objects.all()
    
#     # Debugging: Print all departments and their status
#     for dept in departments:
#         print(f"Department: {dept.dept_name}, Status: {dept.status}")

#     return render(request, 'departments/department_list.html', {'departments': departments})


# # Add Department
# def add_department(request):
#     if request.method == "POST":
#         form = DepartmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Department added successfully!")
#             return redirect('department_list')
#     else:
#         form = DepartmentForm()
#     return render(request, 'departments/department_form.html', {'form': form})

# # Update Department
# def update_department(request, dept_id):
#     department = get_object_or_404(Department, dept_id=dept_id)
#     if request.method == "POST":
#         form = DepartmentForm(request.POST, instance=department)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Department updated successfully!")
#             return redirect('department_list')
#     else:
#         form = DepartmentForm(instance=department)
#     return render(request, 'departments/department_form.html', {'form': form})

# # Soft Delete (Deactivate Department)
# def delete_department(request, dept_id):
#     department = get_object_or_404(Department, dept_id=dept_id)
#     if department.status:
#         department.status = False
#         messages.warning(request, "Department has been deactivated!")
#     else:
#         department.status = True
#         messages.success(request, "Department has been reactivated!")
#     department.save()
#     return redirect('department_list')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from .forms import DepartmentForm
from django.shortcuts import render

def test_view(request):
    return render(request, 'base.html')  # This will check if `base.html` works.

def department_dashboard(request):
    departments = Department.objects.filter(status=True)  # Show only active departments
    return render(request, 'departments/dashboard.html', {'departments': departments})

def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_dashboard')
    else:
        form = DepartmentForm()
    return render(request, 'departments/department_form.html', {'form': form})

def edit_department(request, dept_id):
    department = get_object_or_404(Department, pk=dept_id)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_dashboard')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'departments/department_form.html', {'form': form})

def delete_department(request, dept_id):
    department = get_object_or_404(Department, pk=dept_id)
    department.status = False  # Soft delete (mark as inactive)
    department.save()
    return redirect('department_dashboard')
