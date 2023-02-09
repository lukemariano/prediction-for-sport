# Generated by Django 4.0.5 on 2023-02-09 22:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predicts', '0005_alter_data_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(1.02), django.core.validators.MaxValueValidator(3)]),
        ),
    ]