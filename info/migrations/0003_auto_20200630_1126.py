# Generated by Django 3.0.6 on 2020-06-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20200630_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateField(default='1998-01-01'),
        ),
    ]
