# Generated by Django 4.2.11 on 2024-04-15 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_ports', models.IntegerField()),
                ('available_ports', models.IntegerField()),
                ('is_opening', models.BooleanField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.location')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('model', models.CharField(max_length=100)),
                ('is_payment', models.BooleanField()),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.station')),
            ],
        ),
    ]
