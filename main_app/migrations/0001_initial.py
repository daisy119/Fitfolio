# Generated by Django 4.2.10 on 2024-03-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration', models.DurationField()),
                ('calorie_burnt', models.IntegerField()),
                ('distance', models.FloatField()),
                ('city', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=250)),
                ('max_heart_rate', models.IntegerField()),
            ],
        ),
    ]
