# Generated by Django 2.2.13 on 2020-12-04 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0057_rminvoicecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreport',
            name='month_quarterType',
            field=models.CharField(choices=[('JANUARY', 'JANUARY'), ('FEBRUARY', 'FEBRUARY'), ('MARCH', 'MARCH'), ('APRIL', 'APRIL'), ('MAY', 'MAY'), ('JUNE', 'JUNE'), ('JULY', 'JULY'), ('AUGUST', 'AUGUST'), ('SEPTEMBER', 'SEPTEMBER'), ('OCTOBER', 'OCTOBER'), ('NOVEMBER', 'NOVEMBER'), ('DECEMBER', 'DECEMBER'), ('Q1', 'Q1'), ('Q2', 'Q2')], default=12, max_length=20, verbose_name='Month or Quarter'),
        ),
        migrations.AlterField(
            model_name='rmreport',
            name='month_quarterType',
            field=models.CharField(choices=[('JANUARY', 'JANUARY'), ('FEBRUARY', 'FEBRUARY'), ('MARCH', 'MARCH'), ('APRIL', 'APRIL'), ('MAY', 'MAY'), ('JUNE', 'JUNE'), ('JULY', 'JULY'), ('AUGUST', 'AUGUST'), ('SEPTEMBER', 'SEPTEMBER'), ('OCTOBER', 'OCTOBER'), ('NOVEMBER', 'NOVEMBER'), ('DECEMBER', 'DECEMBER'), ('Q1', 'Q1'), ('Q2', 'Q2'), ('Q3', 'Q3'), ('Q4', 'Q4')], default=12, max_length=20, verbose_name='Month or Quarter'),
        ),
        migrations.CreateModel(
            name='PackageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_branches', models.CharField(choices=[('1', '1-5'), ('2', '5-10'), ('3', '10+')], default='1', max_length=30, verbose_name='Number of Branches')),
                ('number_of_employees', models.CharField(choices=[('1', '1-5'), ('2', '50-100'), ('3', '100+')], default='1', max_length=30, verbose_name='Number of Employees')),
                ('period', models.CharField(choices=[('Monthly', 'Monthly'), ('Yearly', 'Yearly')], default='Monthly', max_length=30, verbose_name='Period')),
                ('price', models.CharField(default='', max_length=10, verbose_name='Price')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webaccount.Sector')),
            ],
        ),
    ]