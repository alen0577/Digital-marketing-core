# Generated by Django 4.0.2 on 2023-04-19 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0018_client_information_am_target_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addi_client_info',
            name='target',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]