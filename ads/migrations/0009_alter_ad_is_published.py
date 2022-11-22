# Generated by Django 4.1.3 on 2022-11-21 15:20

import ads.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0008_alter_ad_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='is_published',
            field=models.BooleanField(default=False, validators=[ads.validators.not_published]),
        ),
    ]
