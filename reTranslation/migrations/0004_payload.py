# Generated by Django 3.2.6 on 2021-08-23 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reTranslation', '0003_auto_20210823_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payloadnumber', models.IntegerField()),
                ('payloadpath', models.CharField(max_length=300)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payloads', to='reTranslation.programs')),
            ],
        ),
    ]
