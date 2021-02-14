# Generated by Django 3.1.5 on 2021-02-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('time', models.DateTimeField()),
                ('address', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('completed', models.CharField(max_length=10)),
                ('writer', models.CharField(max_length=30)),
            ],
        ),
    ]
