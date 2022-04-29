from django.db import models

class Student(models.Model):
    ism=models.CharField(max_length=20)
    yoshi=models.PositiveSmallIntegerField()
    kursi=models.PositiveSmallIntegerField()
    raqami=models.CharField(max_length=15)

    def __str__(self):
        return self.ism

class Reja(models.Model):
    sarlavha=models.CharField(max_length=30)
    sanasi=models.DateField()
    malumot=models.TextField()
    bajarilgan=models.BooleanField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE )
    def __str__(self):
        return f"{self.sarlavha}  {self.malumot}"

