# Generated by Django 4.0.4 on 2022-05-17 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housewars', '0009_alter_activity_session1_signups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='session1_signups',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='session2_signups',
        ),
    ]
