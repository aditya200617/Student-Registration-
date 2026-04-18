from django.db import models
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, blank= True)
    name = models.CharField(max_length= 100)
    age = models.IntegerField()
    address = models.TextField(max_length=100)
    phone_number = models.IntegerField(null= True)
    student_image = models.ImageField(upload_to="student_image", null=True)
    
    
