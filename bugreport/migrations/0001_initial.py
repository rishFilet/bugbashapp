# Generated by Django 3.0 on 2019-12-18 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BashSessionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(choices=[('6s', 'Iphone 6s 20140928'), ('Mini', 'Ipad Mini 20142706'), ('Pixel', 'Google Pixel 20143536')], default=('6s', 'Iphone 6s 20140928'), max_length=50)),
                ('feature', models.CharField(choices=[('Camera', 'Theia / Camera'), ('Tstat', 'Thermostat'), ('Sensors', 'Hecate / Rhodos'), ('Ls', 'Light Switch'), ('Eco_plus', 'Chronos / Eco+'), ('Iris', 'Home monitoring / Iris')], default=('Camera', 'Theia / Camera'), max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ReportFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BugLogStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(choices=[('6s', 'Iphone 6s 20140928'), ('Mini', 'Ipad Mini 20142706'), ('Pixel', 'Google Pixel 20143536')], default=('6s', 'Iphone 6s 20140928'), max_length=50)),
                ('feature', models.CharField(choices=[('Camera', 'Theia / Camera'), ('Tstat', 'Thermostat'), ('Sensors', 'Hecate / Rhodos'), ('Ls', 'Light Switch'), ('Eco_plus', 'Chronos / Eco+'), ('Iris', 'Home monitoring / Iris')], default=('Camera', 'Theia / Camera'), max_length=50)),
                ('summary', models.CharField(max_length=100)),
                ('steps', models.TextField(default='1. \n2.\n3.\n4.', max_length=350)),
                ('result', models.TextField(default='Actual:\n\nExpected:\n', max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
