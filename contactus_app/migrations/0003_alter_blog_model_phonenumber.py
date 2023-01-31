# Generated by Django 4.1.4 on 2022-12-30 04:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_app', '0002_blog_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_model',
            name='phonenumber',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Please Enter Valid Mobile Number', regex='[0-9]{10}')]),
        ),
    ]
