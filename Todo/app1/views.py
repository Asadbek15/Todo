from django.shortcuts import render,redirect
from Todo.app1.models import Reja, Student

def student(request):
    if request.medhod=="GET":
        fa=Student.objects.all()

    if request.medhod=="POST":
        r4 = Student.objects.all()
        r4.ism = request.POST.get("ism")
        r4.yoshi = request.POST.get("y")
        r4.kursi = request.POST.get("k")
        r4.raqami = request.POST.get("r")
        r4.save()
        return redirect("/student/")
    return render(request,"student.html")

def reja(request):
    if request.medhod == "POST":
        f1=Reja.objects.all()
        f1.sarlavha=request.POST.get("s")
        f1.sanasi=request.POST.get("sana")
        f1.malumot=request.POST.get("m")
        f1.bajarilgan=request.POST.get("b")
        f1.save()
        return redirect("/reja/")
    n=Reja.objects.all()
    return render(request,"reja.html",n)

def student_edit(request,pk):
    if request.medhod == "POST":
        r4=Student.objects.get(id=pk)
        r4.ism=request.POST.get("ism")
        r4.yoshi=request.POST.get("y")
        r4.kursi=request.POST.get("k")
        r4.raqami=request.POST.get("r")
        r4.save()
        return redirect("/student/")
    f=Student.objects.get(id=pk)
    return render(request,"student.html",{"student":f})

def reja_edit(request,pl):
    if request.medhod == "POST":
        f1=Reja.objects.get(id=pl)
        f1.sarlavha=request.POST.get("s")
        f1.sanasi=request.POST.get("sana")
        f1.malumot=request.POST.get("m")
        f1.bajarilgan=request.POST.get("b")
        f1.save()
        return redirect("/reja/")
    n=Reja.objects.get(id=pl)
    return render(request,"reja.html",{"reja":n})





# Create your views here.
