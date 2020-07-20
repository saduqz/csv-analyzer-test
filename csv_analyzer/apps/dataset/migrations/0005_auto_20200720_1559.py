# Generated by Django 3.0.7 on 2020-07-20 20:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0004_blog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.AddField(
            model_name='datasetfiles',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 20, 20, 59, 34, 128249, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='DataSetWearerData',
        ),
    ]
