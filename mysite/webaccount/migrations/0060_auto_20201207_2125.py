# Generated by Django 2.2.13 on 2020-12-07 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0059_auto_20201204_1827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packagemodel',
            options={'ordering': ['id'], 'verbose_name': 'Package', 'verbose_name_plural': 'Packages'},
        ),
    ]
