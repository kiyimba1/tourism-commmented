# Generated by Django 3.2.16 on 2022-10-09 08:25

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TouristSites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year_of_inception', models.CharField(max_length=255)),
                ('fee', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact_name', models.CharField(max_length=255)),
                ('popular_stop_overs', models.CharField(max_length=255)),
                ('nearest_main_hospital', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites', to='district.district')),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites', to='district.village')),
            ],
        ),
    ]
