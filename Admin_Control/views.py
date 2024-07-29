from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import Doctor_Add_Form
from .models import Doctor_Add_Model

# Create your views here.

def Your_Profile_Page(request):
    if request.POST:
        form=Doctor_Add_Form(request.POST)
        if form.is_valid():
            name=                    form.cleaned_data.get("name")
            last_name=               form.cleaned_data.get("last_name")
            email=                   form.cleaned_data.get("email")
            tel=                     form.cleaned_data.get("tel")
            about_me=                form.cleaned_data.get("about_me")
            my_skills=               form.cleaned_data.get("my_skills")
            education=               form.cleaned_data.get("education")
            education_start_years=   form.cleaned_data.get("education_start_years")
            education_grad_years=    form.cleaned_data.get("education_grad_years")
            speciality=              form.cleaned_data.get("speciality")
            experiance_start_years=  form.cleaned_data.get("experiance_start_years")
            experiance_finish_years= form.cleaned_data.get("experiance_finish_years")
            new_doctor=Doctor_Add_Model(name=name, last_name=last_name, email=email, tel=tel, about_me=about_me, my_skills=my_skills, education=education,education_start_years=education_start_years, education_grad_years=education_grad_years, speciality=speciality,experiance_start_years=experiance_start_years, experiance_finish_years=experiance_finish_years)
            new_doctor.save()
            return redirect("Home")
    form=Doctor_Add_Form()
    context={"form":form}
    return render(request,"your_profile.html",context)
