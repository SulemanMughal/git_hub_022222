# Generated by Django 2.2.12 on 2020-05-07 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0027_auto_20200507_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickuprequestorders',
            name='client',
            field=models.ForeignKey(limit_choices_to={'status': 'Active'}, on_delete=django.db.models.deletion.CASCADE, to='webaccount.Client_Personal_Info'),
        ),
    ]
