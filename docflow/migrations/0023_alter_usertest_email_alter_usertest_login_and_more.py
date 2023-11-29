# Generated by Django 4.2.6 on 2023-11-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docflow', '0022_rename_mail_usertest_email_alter_department_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertest',
            name='email',
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='login',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]
