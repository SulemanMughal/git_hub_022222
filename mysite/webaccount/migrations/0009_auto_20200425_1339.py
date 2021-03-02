# Generated by Django 2.2.12 on 2020-04-25 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0008_consulatationrequest_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultantmodel',
            name='parentField',
            field=models.CharField(blank=True, default=None, error_messages={'unique': 'Parent Field Already Exists.'}, max_length=100, null=True, unique=True, verbose_name='Parent Field'),
        ),
        migrations.AlterField(
            model_name='consultantmodel',
            name='Name',
            field=models.CharField(default=None, error_messages={'blank': 'Name is required', 'unique': 'Name Already Exists.'}, max_length=100, unique=True, verbose_name='Field'),
        ),
    ]
