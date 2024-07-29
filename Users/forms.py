from django import forms

class SignUp(forms.Form):
    firstname=  forms.CharField( label="First Name",max_length=15, required=True, widget=forms.TextInput(    attrs={'class':'signup_input'}))
    lastname=   forms.CharField( label="Last Name", max_length=15, required=True, widget=forms.TextInput(    attrs={'class':'signup_input'}))
    email=      forms.CharField( label="Email ",    max_length=25, required=True, widget=forms.TextInput(    attrs={'class':'signup_input'}))
    password=   forms.CharField( label="Password",  max_length=30, required=True, widget=forms.PasswordInput(attrs={'class':'signup_input'}))
    repassword= forms.CharField( label="Repasword", max_length=15, required=True, widget=forms.PasswordInput(attrs={'class':'signup_input'}))

def clean(self):
    firstname= self.cleaned_data["firstname"]
    lastname=  self.cleaned_data['lastname']
    email=     self.cleaned_data['email']
    password=  self.cleaned_data["password"]
    repassword=self.cleaned_data["repassword"]
    if password and repassword and password != repassword:
                   raise forms.ValidationError("passwords does not match")
    value={"firstname":firstname,"lastname":lastname,"email":email,"password":password}
    return value


class Log_In(forms.Form):
    email=    forms.CharField( label="Email", max_length=30,    widget=forms.TextInput(attrs={'class':'login_input'}))
    password= forms.CharField( label="Password", max_length=30, widget=forms.TextInput(attrs={'class':'login_input'}))
