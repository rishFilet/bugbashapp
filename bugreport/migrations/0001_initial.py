# Generated by Django 3.0 on 2019-12-14 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BugLogStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(choices=[('6s', 'Iphone 6s 20140928'), ('Mini', 'Ipad Mini 20142706')], default=('6s', 'Iphone 6s 20140928'), max_length=50)),
                ('feature', models.CharField(choices=[('Camera', 'Theia/Camera'), ('Tstat Reg', 'Tstat Registration')], default=('Camera', 'Theia/Camera'), max_length=50)),
                ('summary', models.CharField(max_length=100)),
                ('steps', models.CharField(max_length=100)),
                ('result', models.TextField(default='Enter a descriptive result here', max_length=500)),
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
            name='fields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
