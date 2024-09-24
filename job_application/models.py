from django.db import models

# commands to create the database
# python manage.py makemigrations
# this command created 0001_initial.py inside migrations
# python manage.py migrate
# this command alters the databse executing the code in 0001_initial.py
# now the database has been modified with the desired table(s)

class Form(models.Model):
    # create database model with the columns
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"