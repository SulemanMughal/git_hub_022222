# Generated by Django 2.2.12 on 2020-05-05 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200505_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.CharField(blank=True, choices=[(True, 'Admin'), (False, 'Relational Manager'), ('Consultant', 'Consultant')], default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', max_length=11, null=True, verbose_name='superuser status'),
        ),
    ]
