# Generated by Django 4.0.3 on 2022-04-25 07:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0002_licensepurchase_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licensepurchase',
            name='no_of_licenses_purchased',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)]),
        ),
    ]