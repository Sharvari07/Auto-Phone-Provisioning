# Generated by Django 2.2 on 2019-07-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pull', '0003_auto_20190718_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call_details',
            name='call_duration',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='call_details',
            name='called_party_dir_num',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
