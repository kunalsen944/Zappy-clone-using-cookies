# Generated by Django 2.1.1 on 2018-10-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zappyapp', '0017_auto_20181030_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pid',
            field=models.ManyToManyField(blank=True, default='', to='zappyapp.Product'),
        ),
    ]
