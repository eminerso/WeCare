from django import forms

class Doctor_Add_Form(forms.Form):
    name=                   forms.CharField(  label= "Name",                    max_length= 20)
    last_name=              forms.CharField(  label= "Last Name",               max_length=20)
    email=                  forms.EmailField( label= "Email" ,                  max_length= 30)
    tel=                    forms.CharField(  label= "Tel",                     max_length= 20)
    education=              forms.CharField(  label= "Education",               max_length= 60)
    speciality=             forms.CharField(  label= "Speciality",              max_length= 80)
    education_start_years=  forms.DateField(  label= "Education Start Year"  ,  widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]) 
    education_grad_years=   forms.DateField(  label= "Education Graduate year", widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"])
    experiance_start_years= forms.DateField(  label= "Experiance Start year" ,  widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"])
    experiance_finish_years=forms.DateField(  label= "Experiance Finish year" , widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"])
    about_me=               forms.CharField(  label= "About Doctor",            max_length= 600, widget=forms.Textarea(attrs={"rows":"5"}))
    my_skills=              forms.CharField(  label= "Doctors Skills",          max_length= 600, widget=forms.Textarea(attrs={"rows":"5"}))
    
   
