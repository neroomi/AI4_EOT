# Generated by Django 3.1.6 on 2021-02-10 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='start_time',
            new_name='time',
        ),
    ]