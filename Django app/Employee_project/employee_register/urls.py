from django.urls import path,include
from . import views #everything from the views name would be imported from here
urlpatterns = [
    path('', views.employee_form),
    path('list/',views.employee_list)
]