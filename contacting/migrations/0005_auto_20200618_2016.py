# Generated by Django 3.0.7 on 2020-06-18 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacting', '0004_auto_20200618_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='code',
            field=models.CharField(default='00-000', max_length=6),
        ),
    ]
