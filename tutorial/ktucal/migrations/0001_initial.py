# Generated by Django 4.1.7 on 2023-03-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rollno', models.CharField(max_length=255)),
                ('Semester_1', models.IntegerField(default=0)),
                ('Semester_2', models.IntegerField(default=0)),
                ('Semester_3', models.IntegerField(default=0)),
                ('Semester_4', models.IntegerField(default=0)),
            ],
        ),
    ]
