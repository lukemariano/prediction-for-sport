# Generated by Django 4.0.5 on 2023-02-09 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predicts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='chupisco',
        ),
    ]