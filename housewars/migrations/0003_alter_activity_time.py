# Generated by Django 4.0.4 on 2022-09-03 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housewars', '0002_alter_pointsentry_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.IntegerField(choices=[(30, '30'), (60, '60')]),
        ),
    ]
