# Generated by Django 3.1.6 on 2021-02-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todayweather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('temp', models.DecimalField(decimal_places=1, max_digits=3)),
                ('feels_like', models.DecimalField(decimal_places=1, max_digits=3)),
                ('temp_min', models.DecimalField(decimal_places=1, max_digits=3)),
                ('temp_max', models.DecimalField(decimal_places=1, max_digits=3)),
                ('weather_desc', models.CharField(max_length=100)),
                ('hmdt', models.DecimalField(decimal_places=1, max_digits=3)),
                ('wind_spd', models.DecimalField(decimal_places=2, max_digits=3)),
                ('date_time', models.DateTimeField()),
                ('sunrise', models.DateTimeField()),
                ('sunset', models.DateTimeField()),
                ('pm2_5', models.DecimalField(decimal_places=2, max_digits=3)),
                ('pm10', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]