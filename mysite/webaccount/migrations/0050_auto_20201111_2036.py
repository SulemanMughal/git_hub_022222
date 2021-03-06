# Generated by Django 2.2.13 on 2020-11-11 15:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0049_auto_20201018_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreport',
            name='month_quarterType',
            field=models.CharField(choices=[('JANUARY', 'JANUARY'), ('FEBRUARY', 'FEBRUARY'), ('MARCH', 'MARCH'), ('APRIL', 'APRIL'), ('MAY', 'MAY'), ('JUNE', 'JUNE'), ('JULY', 'JULY'), ('AUGUST', 'AUGUST'), ('SEPTEMBER', 'SEPTEMBER'), ('OCTOBER', 'OCTOBER'), ('NOVEMBER', 'NOVEMBER'), ('DECEMBER', 'DECEMBER'), ('Q1', 'Q1'), ('Q2', 'Q2')], default=11, max_length=20, verbose_name='Month or Quarter'),
        ),
        migrations.AlterField(
            model_name='rmreport',
            name='month_quarterType',
            field=models.CharField(choices=[('JANUARY', 'JANUARY'), ('FEBRUARY', 'FEBRUARY'), ('MARCH', 'MARCH'), ('APRIL', 'APRIL'), ('MAY', 'MAY'), ('JUNE', 'JUNE'), ('JULY', 'JULY'), ('AUGUST', 'AUGUST'), ('SEPTEMBER', 'SEPTEMBER'), ('OCTOBER', 'OCTOBER'), ('NOVEMBER', 'NOVEMBER'), ('DECEMBER', 'DECEMBER'), ('Q1', 'Q1'), ('Q2', 'Q2'), ('Q3', 'Q3'), ('Q4', 'Q4')], default=11, max_length=20, verbose_name='Month or Quarter'),
        ),
        migrations.CreateModel(
            name='RMInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submittingDate', models.DateField(default=django.utils.timezone.now, verbose_name='Submitting Date')),
                ('statusType', models.CharField(choices=[('New', 'New'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Processing', 'Processing'), ('Pending', 'Pending')], default='New', max_length=15, verbose_name='Status')),
                ('lastUpdate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last Update')),
                ('uploadFile', models.FileField(upload_to='uploads/rmInvoice/%Y/%m/%d/', verbose_name='Upload Image')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webaccount.Client_Personal_Info')),
            ],
            options={
                'verbose_name': 'Client Invoice',
                'verbose_name_plural': 'Client Invoices',
            },
        ),
    ]
