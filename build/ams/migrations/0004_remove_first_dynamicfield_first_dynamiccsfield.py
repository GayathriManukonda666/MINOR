# Generated by Django 4.2 on 2023-04-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0003_remove_first_dynamic_field_first_dynamicfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='first',
            name='dynamicfield',
        ),
        migrations.AddField(
            model_name='first',
            name='dynamiccsfield',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
