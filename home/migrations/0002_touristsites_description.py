# Generated by Django 3.2.16 on 2022-10-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristsites',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]