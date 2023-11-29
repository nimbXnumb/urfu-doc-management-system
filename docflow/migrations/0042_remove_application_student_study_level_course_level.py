# Generated by Django 4.2.6 on 2023-11-29 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docflow', '0041_application_student_study_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='student_study_level',
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='docflow.studylevel'),
        ),
    ]
