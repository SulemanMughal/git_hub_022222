# Generated by Django 2.2.12 on 2020-05-05 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0021_auto_20200506_0007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consultantmodel',
            options={'ordering': ['-id'], 'verbose_name': 'Consultation Field', 'verbose_name_plural': 'Consultation Fields'},
        ),
    ]
