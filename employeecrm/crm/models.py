from django.db import models

# Create your models here.

class Employee(models.Model):

    name=models.CharField(max_length=200)

    email=models.EmailField(unique=True)

    address=models.TextField()

    department=models.CharField(max_length=200)

    salary=models.PositiveIntegerField()

    date_of_join=models.DateField()

    gender_options=(
        ("male","male"),
        ("female","female")
    )

    gender=models.CharField(max_length=200,choices=gender_options,default="male")

    picture=models.ImageField(upload_to="employee_image",null=True,blank=True)

    def __str__(self):
        return self.name
