# Generated by Django 4.2.10 on 2024-02-11 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ydd_db', '0002_rename_mealitem_meal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='meal_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='meal',
            old_name='meal_name',
            new_name='name',
        ),
    ]
