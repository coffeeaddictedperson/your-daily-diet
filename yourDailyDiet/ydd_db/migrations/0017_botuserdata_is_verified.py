# Generated by Django 4.2.10 on 2024-02-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ydd_db', '0016_alter_botuserdata_bot_valid_till'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuserdata',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
