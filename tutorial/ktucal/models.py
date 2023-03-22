from django.db import models

# Create your models here.
class result(models.Model):
    Name = models.CharField(max_length=255)
    Rollno = models.CharField(max_length=255)
    Semester_1=models.FloatField(default=0)
    Semester_2=models.FloatField(default=0)
    Semester_3=models.FloatField(default=0)
    Semester_4=models.FloatField(default=0)
    Semester_5=models.FloatField(default=0)
    Semester_6=models.FloatField(default=0)
    Semester_7=models.FloatField(default=0)
    Semester_8=models.FloatField(default=0)
    Total_Credit=models.IntegerField(default=160)
    Total_CGPA=models.FloatField(default=0)
