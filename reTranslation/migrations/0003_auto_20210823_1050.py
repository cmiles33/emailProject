# Generated by Django 3.2.6 on 2021-08-23 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reTranslation', '0002_auto_20210823_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programs',
            name='endTime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='programs',
            name='startTime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
