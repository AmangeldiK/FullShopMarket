# Generated by Django 3.0.8 on 2020-08-03 06:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200803_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 8, 3, 6, 28, 35, 353687, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
