from django.db import models

# Create your models here.

# For any model tere will be Django Primary key that will be created by Django ORM itself,
# It will be 'id', 
# It will start from 1 and incremented by 1 upon new record insertion. 
# It is managed by Django ORM itself.
#Position model with property as title
class Position(models.Model):
    title = models.CharField(max_length=50)
#Employee Model
class Employee(models.Model):
    #specify model properties
    fullname = models.CharField(max_length=100) #set maximum number of characyter length
    emp_code = models.CharField(max_length=4)
    Contact = models.CharField(max_length=15)
    Position = models.ForeignKey(Position, on_delete=models.CASCADE) #depend on other table and have to create corressponding model class
    # No. of Employeement years = models.Charfield(max_length=100)
    

