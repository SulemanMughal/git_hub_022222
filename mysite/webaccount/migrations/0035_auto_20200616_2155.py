# Generated by Django 2.2.13 on 2020-06-16 16:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0034_auto_20200511_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreport',
            name='month_quarterType',
            field=models.CharField(choices=[('JANUARY', 'JANUARY'), ('FEBRUARY', 'FEBRUARY'), ('MARCH', 'MARCH'), ('APRIL', 'APRIL'), ('MAY', 'MAY'), ('JUNE', 'JUNE'), ('JULY', 'JULY'), ('AUGUST', 'AUGUST'), ('SEPTEMBER', 'SEPTEMBER'), ('OCTOBER', 'OCTOBER'), ('NOVEMBER', 'NOVEMBER'), ('DECEMBER', 'DECEMBER'), ('Q1', 'Q1'), ('Q2', 'Q2')], default=6, max_length=20, verbose_name='Month or Quarter'),
        ),
        migrations.CreateModel(
            name='RMReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportType', models.CharField(choices=[('VAT Report', 'VAT Report'), ('Ratio Analysis Report', 'Ratio Analysis Report')], default='Report Type', max_length=25)),
                ('dateYear', models.IntegerField(choices=[(2025, 2025), (2024, 2024), (2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981)], default=2020, validators=[django.core.validators.MinValueValidator(1980), django.core.validators.MaxValueValidator(2025)], verbose_name='Year')),
                ('month_quarterType', models.CharField(choices=[('JANUARY', 'JANUARY'), ('FEBRUARY', 'FEBRUARY'), ('MARCH', 'MARCH'), ('APRIL', 'APRIL'), ('MAY', 'MAY'), ('JUNE', 'JUNE'), ('JULY', 'JULY'), ('AUGUST', 'AUGUST'), ('SEPTEMBER', 'SEPTEMBER'), ('OCTOBER', 'OCTOBER'), ('NOVEMBER', 'NOVEMBER'), ('DECEMBER', 'DECEMBER'), ('Q1', 'Q1'), ('Q2', 'Q2')], default=6, max_length=20, verbose_name='Month or Quarter')),
                ('uploadFile', models.FileField(blank=True, upload_to='uploads/rmReports/%Y/%m/%d/', verbose_name='Upload Document')),
                ('finalReportIssueDate', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webaccount.Client_Personal_Info')),
            ],
            options={
                'verbose_name': 'Client Report',
                'verbose_name_plural': 'Client Reports',
            },
        ),
    ]
