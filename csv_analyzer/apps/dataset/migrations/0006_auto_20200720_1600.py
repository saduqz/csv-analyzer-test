# Generated by Django 3.0.7 on 2020-07-20 21:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0005_auto_20200720_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetfiles',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
