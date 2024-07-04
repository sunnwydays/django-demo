from django.db import models

# also remember to add to settings.py
# makemigrations, showmigrations, migrate, sqlmigrate
# CreateModel, DeleteModel, AddField, RemoveField, AlterField, RenameField, RenameModel, AddIndex
class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()