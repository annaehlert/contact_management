# Generated by Django 3.0.7 on 2020-06-18 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacting', '0003_user_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='code',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='address',
            name='house_nr',
            field=models.IntegerField(default=1),
        ),
    ]
