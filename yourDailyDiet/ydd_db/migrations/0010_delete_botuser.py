# Generated by Django 4.2.10 on 2024-02-17 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ydd_db', '0009_remove_botuser_identification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BotUser',
        ),
    ]