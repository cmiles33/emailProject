# Generated by Django 3.2.6 on 2021-09-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reTranslation', '0002_programpicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='photo',
            field=models.ImageField(blank=True, upload_to='programs/'),
        ),
        migrations.DeleteModel(
            name='ProgramPicture',
        ),
    ]
