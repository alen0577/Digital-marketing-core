# Generated by Django 4.1.4 on 2023-06-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0074_alter_daily_leeds_exists_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_leeds_exists',
            name='executive',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]