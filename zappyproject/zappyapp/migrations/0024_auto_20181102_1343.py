# Generated by Django 2.1.1 on 2018-11-02 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zappyapp', '0023_auto_20181031_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cust_address',
            field=models.CharField(default=None, max_length=400),
        ),
    ]
