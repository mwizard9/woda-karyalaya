# Generated by Django 4.0.4 on 2022-08-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wodakaryalaya', '0003_birth_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birth',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10),
        ),
    ]
