# Generated by Django 2.2.12 on 2020-04-25 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0002_clientrequireddocuments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulatationrequest',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webaccount.ConsultantModel', verbose_name='Consultation Field'),
        ),
    ]
