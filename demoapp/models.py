from django.db import models

# also remember to add to settings.py
# makemigrations, showmigrations, migrate, sqlmigrate
# CreateModel, DeleteModel, AddField, RemoveField, AlterField, RenameField, RenameModel, AddIndex
# Create

class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name
# admin lemonAdmin@3!
# jason_chef lemonChef@123!

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name



# migrating and adding an entry with models
# Djangovenv\Scripts\Activate
# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
# >>> from demoapp.models import DrinksCategory
# >>> c = DrinksCategory(category_name="coffee")
# >>> c.save()
# >>> fk = DrinksCategory.objects.get(pk=1)
# >>> from demoapp.models import Drinks
# >>> d = Drinks(drink_name='mocha',price=7,category_id=fk)  
# >>> d.save()

# ORM / QuerySet
# Create (INSERT)
# >>> c=Customer.objects.get(name="Henry") 
# >>> Vehicle.objects.create(name="Ford", customer=c)
# Read (SELECT, WHERE)
# >> lst=Customer.objects.all()  
# mydata = Customer.objects.filter(name__startswith='H') 
# Update
# >>> c=Customer.objects.get(name="Henry") 
# >>> c.name="Helen" 
# >>> c.save() 
# Delete (DELETE)
# >>> c=Customer.objects.get(pk=4) 
# >>> c.delete() 