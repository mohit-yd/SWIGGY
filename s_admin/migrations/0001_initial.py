# Generated by Django 3.0.3 on 2020-04-15 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLogi6nModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('otp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('state_no', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('city_no', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_admin.StateModel')),
            ],
        ),
        migrations.CreateModel(
            name='AreaModel',
            fields=[
                ('area_no', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_admin.CityModel')),
            ],
        ),
    ]
