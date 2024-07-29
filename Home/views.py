from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home_page(request):
    return render(request,"home.html")

def All_Services_Page(request):
    return render(request,"all_services.html")

def Service_Detail_Page(request):
    return render(request,"service_detail.html")

def Blog_Page(request):
    return render(request,"blog.html")

def Contact_Page(request):
    return render(request,"contact_us.html")

def Doctors_Page(request):
    return render(request,"doctors.html")

def Doctor_Detail_Page(request):
    return render(request,"doctor_detail.html")

def Blog_Detail_Page(request):
    return render(request,"blog_detail.html")


