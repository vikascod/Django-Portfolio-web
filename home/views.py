from django.shortcuts import render, HttpResponse
from home.models import Person

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name, email, phone, desc)
        ins = Person(name=name, email=email, phone=phone, desc=desc)
        ins.save()

    return render(request, 'contact.html')