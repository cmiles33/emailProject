# Generated by Django 3.2.6 on 2021-08-23 15:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reTranslation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programs',
            name='endTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='programs',
            name='startTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
