from django.shortcuts import render

# Create your views here.
# Define view function and display all the employee records
def employee_list(request):
    return render (request, "employee_register/employee_list.html")
# This is for insert  operation
def employee_form(request):
    return render (request, "employee_register/employee_form.html")
# This is for delete function
# def employee_delete(request):
#     return


