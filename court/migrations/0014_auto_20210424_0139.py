# Generated by Django 3.1.7 on 2021-04-23 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0013_auto_20210424_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='docs',
            field=models.FileField(blank=True, null=True, upload_to='media/casedocs'),
        ),
    ]
