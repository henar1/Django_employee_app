# Django_employee_app

Install python IDE
pip install django

django-admin startproject example (for mac)
In order to run django application, 
FOLLOW THIS on terminal
a. set up new virtual environment, by:
   sudo pip3 install virtualenv
   source newenv/bin/activate
   pip3 install django
b. python3 manage.py runserver
c. it will point to the local host (http://127.0.0.1:8000/)


# Create Emaloyment Management app using CRUD operation
1. open seperate Terminal, 
   run: python3 manage.py startapp employee_register
   
2. create a appstructure.txt inside employee_register
3. within Employee_project>settings.py
   Add: 'employee_register' inside INSTALLED APP space
   
4. Install Postgressql along with pgadmin
   Set the server
   
5. python3 manage.py migrate  
6. Start with Manage.py file in employee_register.
7. After that migrate "python3 manage.py makemigrations employee_register"
   migration folder will be created within employee_register app will start and these two aspects will be created
    - Create model Position
    - Create model Employee
8. Now we need to provide migration with sql
    'python3 manage.py sqlmigrate employee_register 0001'
     python3 manage.py sqlmigrate app_name 0001
     
 9. In order to execute the SQL script that we have recieved
    Execute: python3 manage.py migrate
 10. After execution same will be modifies in PGAdmin database
 11. Now start with view function
     employee_regioster>views.py
 12. Set path in Employee_project> urls.py
 13. all the requests which starts with 'employee/' will be handeled inside the newely created file inside 'employee_register>urls.py'
 14. For executing these urls we need to create template
 15. Inside employee_register>template>employee_register>templates
     Create three template:
     - base.html (parent template)
     - employee_list.html (child template)
     - employee_form.html (child template)
  
 16. Bootstrap style sheets
 17. 
     
 


   

 