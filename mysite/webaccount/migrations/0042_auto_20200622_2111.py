# Generated by Django 2.2.13 on 2020-06-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0041_auto_20200622_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rmreport',
            name='status',
            field=models.CharField(choices=[('Not Confirmed', 'Not Confirmed'), ('Confirmed', 'Confirmed')], default='Not Confirmed', max_length=15),
        ),
    ]