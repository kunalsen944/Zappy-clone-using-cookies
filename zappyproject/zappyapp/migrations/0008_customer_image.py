# Generated by Django 2.1.1 on 2018-10-26 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zappyapp', '0007_auto_20181026_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='Products/profile_pics'),
        ),
    ]
