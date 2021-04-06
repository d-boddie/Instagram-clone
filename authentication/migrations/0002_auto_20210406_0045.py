# Generated by Django 3.1.7 on 2021-04-06 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramuser',
            name='bio',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='instagramuser',
            name='website',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
