# Generated by Django 3.1.7 on 2021-04-14 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
        ('photo', '0003_auto_20210414_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='comment.comment'),
        ),
    ]