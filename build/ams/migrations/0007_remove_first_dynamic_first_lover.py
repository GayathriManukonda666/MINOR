# Generated by Django 4.2 on 2023-04-28 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0006_remove_first_dynamiccsfield2_first_dynamic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='first',
            name='dynamic',
        ),
        migrations.AddField(
            model_name='first',
            name='lover',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
