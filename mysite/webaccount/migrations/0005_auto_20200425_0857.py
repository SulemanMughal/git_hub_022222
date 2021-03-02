# Generated by Django 2.2.12 on 2020-04-25 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0004_consulatationrequest_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulatationrequest',
            old_name='client_paid',
            new_name='clientPaid',
        ),
        migrations.RemoveField(
            model_name='consulatationrequest',
            name='client_paid_all_amount',
        ),
        migrations.AddField(
            model_name='consulatationrequest',
            name='clientPaidAllAmount',
            field=models.BooleanField(default=False, verbose_name='Client Paid All Amount'),
        ),
    ]
