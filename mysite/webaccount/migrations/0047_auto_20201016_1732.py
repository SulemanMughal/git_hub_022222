# Generated by Django 2.2.13 on 2020-10-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0046_auto_20201007_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='rmreport',
            name='chartData_2',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Chart 2 Saved Data'),
        ),
        migrations.AddField(
            model_name='rmreport',
            name='chartLabel_2',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Chart 2 Saved Fields'),
        ),
        migrations.AddField(
            model_name='rmreport',
            name='is_saved_chart_2',
            field=models.BooleanField(default=False, verbose_name='Is Chart 2 saved?'),
        ),
    ]
