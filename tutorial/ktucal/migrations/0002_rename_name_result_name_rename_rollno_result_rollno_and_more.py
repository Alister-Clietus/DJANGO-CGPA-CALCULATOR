# Generated by Django 4.1.7 on 2023-03-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ktucal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='rollno',
            new_name='Rollno',
        ),
        migrations.AddField(
            model_name='result',
            name='Semester_5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='Semester_6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='Semester_7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='Semester_8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='Total_CGPA',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='Total_Credit',
            field=models.IntegerField(default=160),
        ),
    ]
