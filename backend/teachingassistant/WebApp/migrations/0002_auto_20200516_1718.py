# Generated by Django 2.2.8 on 2020-05-16 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='duedate',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 16, 17, 18, 42, 354127)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 16, 17, 18, 42, 356149)),
        ),
        migrations.AlterField(
            model_name='stringfield',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 16, 17, 18, 42, 355147)),
        ),
    ]
