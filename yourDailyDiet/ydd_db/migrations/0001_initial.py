# Generated by Django 4.2.9 on 2024-02-08 20:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MealItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('meal_name', models.CharField(max_length=50, unique=True)),
                ('meal_description', models.CharField(max_length=255)),
                ('meal_type', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner'), ('S', 'Snack'), ('O', 'Other')], default='D', max_length=1)),
                ('is_vegetarian', models.BooleanField()),
            ],
        ),
    ]
