# Generated by Django 3.0 on 2019-12-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('rank', models.PositiveIntegerField(blank=True, default=0, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('iOS', models.PositiveIntegerField(blank=True, default=0)),
                ('Android', models.PositiveIntegerField(blank=True, default=0)),
                ('TSTAT', models.PositiveIntegerField(blank=True, default=0)),
                ('CAMERA', models.PositiveIntegerField(blank=True, default=0)),
                ('SENSORS', models.PositiveIntegerField(blank=True, default=0)),
                ('SWITCH', models.PositiveIntegerField(blank=True, default=0)),
                ('ECO_PLUS', models.PositiveIntegerField(blank=True, default=0)),
                ('total', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
    ]
