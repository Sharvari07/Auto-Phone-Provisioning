# Generated by Django 2.2 on 2019-07-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pull', '0002_auto_20190718_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call_details',
            name='called_party_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
