# Generated by Django 2.2.13 on 2020-11-18 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webaccount', '0056_remove_rminvoice_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='RMInvoiceComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webaccount.RMInvoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
