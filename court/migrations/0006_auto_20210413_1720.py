# Generated by Django 3.1.7 on 2021-04-13 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0005_case_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge',
            name='district',
            field=models.CharField(max_length=100),
        ),
    ]
