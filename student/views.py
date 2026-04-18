from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index (request):
    return render(request,"index.html")

def add_show(request):
    print("------------- show ----------")
    if request.method == "POST":
        data = request.POST
        print("------------", data)
        name = data.get('name')
        age = data.get('age')
        address = data.get('address')
        phone_number = data.get('phone_number')
        student_image = request.FILES.get('student_image')

        student = Student(name= name, age= age, address= address, phone_number= phone_number, student_image= student_image)
        student.save()
        return redirect('/')
    
    queryset = Student.objects.all()
    context = {'students': queryset}
    print("---------- test -----", context)
    return render(request,'addandshow.html', context)


def update_student(request,id):
    student = Student.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        age = data.get('age')
        address = data.get('address')
        phone_number = data.get('phone')
        student_image = request.FILES.get('photo')
        student.name = name
        student.age = age
        student.address = address
        student.phone_number = phone_number

        if student_image:
            student.photo = student_image

        student.save()
        return redirect('/')

    context = {'student': student}
    return render(request,'update_student.html',context)



def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect ('/')


