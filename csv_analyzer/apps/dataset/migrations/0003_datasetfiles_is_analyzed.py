# Generated by Django 3.0.7 on 2020-07-13 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0002_auto_20200712_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetfiles',
            name='is_analyzed',
            field=models.BooleanField(default=False),
        ),
    ]