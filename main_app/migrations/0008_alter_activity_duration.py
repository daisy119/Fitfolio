# Generated by Django 4.2.11 on 2024-03-07 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_activity_activity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='duration',
            field=models.DurationField(verbose_name='Activity duration'),
        ),
    ]
