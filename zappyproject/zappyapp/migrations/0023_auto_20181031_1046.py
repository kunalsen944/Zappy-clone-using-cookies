# Generated by Django 2.1.1 on 2018-10-31 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zappyapp', '0022_auto_20181031_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
