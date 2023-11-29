# Generated by Django 4.2.6 on 2023-11-28 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docflow', '0037_rename_course_number_course_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='docflow.studylevel'),
            preserve_default=False,
        ),
    ]
