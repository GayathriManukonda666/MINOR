# Generated by Django 4.2 on 2023-05-03 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0013_e2csecse2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credentials',
            name='id',
        ),
        migrations.AlterField(
            model_name='credentials',
            name='username',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
