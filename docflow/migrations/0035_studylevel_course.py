# Generated by Django 4.2.6 on 2023-11-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docflow', '0034_remove_course_study_level_delete_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studylevel',
            name='course',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
