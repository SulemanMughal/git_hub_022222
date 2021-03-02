# Generated by Django 2.2.13 on 2020-12-20 10:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0061_auto_20201220_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagemodel',
            name='price',
            field=models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0, message='Value should be greater than 0.')], verbose_name='Price'),
        ),
    ]