from django.db import models

# Create your models here.
class Doctor_Add_Model(models.Model):
    name=                   models.CharField(  max_length= 20)
    last_name=              models.CharField(  max_length= 20)
    email=                  models.EmailField( max_length= 30)
    tel=                    models.CharField(  max_length= 20)
    about_me=               models.TextField(  max_length= 600)
    my_skills=              models.TextField(  max_length= 600)
    education=              models.CharField(  max_length= 60)
    education_start_years=  models.DateField(  max_length= 80)
    education_grad_years=   models.DateField(  max_length= 80)
    speciality=             models.CharField(  max_length= 80)
    experiance_start_years= models.DateField(  max_length= 80)
    experiance_finish_years=models.DateField(  max_length= 80)
    def __str__(self):
        return self.name

