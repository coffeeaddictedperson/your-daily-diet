# Generated by Django 4.2.10 on 2024-02-17 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ydd_db', '0014_botuserdata_is_suspended_botuserdata_requests_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuserdata',
            name='bot_valid_till',
            field=models.DateTimeField(),
        ),
    ]
