from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import SignUp
from django.contrib.auth import login
from django.contrib.auth import get_user_model
User = get_user_model()


from django.contrib.auth import authenticate,login,logout
from .forms import Log_In


# Create your views here.
def SignUp_Page(request):
    form=SignUp(request.POST or None)


    if form.is_valid():
        firstname=form.cleaned_data.get("firstname")
        lastname= form.cleaned_data.get("lastname")
        email=    form.cleaned_data.get("email")
        password= form.cleaned_data.get("password")
        

        newUser=User.objects.create_user(username=firstname,first_name=firstname,last_name=lastname, email=email, password=password)
        newUser.username=firstname
        newUser.first_name=firstname
        newUser.last_name= lastname
        newUser.email=email
        newUser.set_password=password
        newUser.save()
        login(request, newUser)
        return redirect("Home")
    
    context={"form":form}
    return render(request,"signup.html",context)



def Login_Page(request):
   form=Log_In(request.POST or None)
   context={"form":form}
   if form.is_valid():
      email=    form.cleaned_data.get("email")  
      password= form.cleaned_data.get("password")
      user=authenticate(email=email,password =password)
      if user is None:
         return render(request,"login.html")
      login(request, user)
      return redirect("Home")
      
   return render(request,"login.html", context)





def Log_Out_Page(request):
   logout(request)
   return redirect('Login')




