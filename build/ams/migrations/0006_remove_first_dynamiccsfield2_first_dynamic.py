# Generated by Django 4.2 on 2023-04-28 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0005_rename_dynamiccsfield_first_dynamiccsfield2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='first',
            name='dynamiccsfield2',
        ),
        migrations.AddField(
            model_name='first',
            name='dynamic',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
