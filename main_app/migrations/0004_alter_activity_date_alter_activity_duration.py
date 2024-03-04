# Generated by Django 4.2.10 on 2024-03-04 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_activity_activity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(verbose_name='Activity date'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='duration',
            field=models.DurationField(verbose_name='Activity duration'),
        ),
    ]