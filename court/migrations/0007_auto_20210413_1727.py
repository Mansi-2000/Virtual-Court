# Generated by Django 3.1.7 on 2021-04-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0006_auto_20210413_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge',
            name='district',
            field=models.CharField(max_length=500),
        ),
    ]
