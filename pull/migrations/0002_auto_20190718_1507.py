# Generated by Django 2.2 on 2019-07-18 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pull', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call_details',
            name='called_party_dir_num',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='call_details',
            name='called_party_name',
            field=models.CharField(max_length=20),
        ),
    ]
