# Generated by Django 2.2.12 on 2020-05-05 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0017_consultantmanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulatationrequest',
            name='consultantManager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webaccount.consultantManager', verbose_name='Consultant Manager'),
        ),
    ]