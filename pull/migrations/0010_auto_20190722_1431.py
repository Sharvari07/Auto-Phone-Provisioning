# Generated by Django 2.2 on 2019-07-22 09:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pull', '0009_auto_20190722_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polycomipphone',
            name='time_stamp',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
