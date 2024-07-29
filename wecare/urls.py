
from django.contrib import admin
from django.urls    import path
from Home.views     import Home_page, Contact_Page, All_Services_Page, Blog_Page, Service_Detail_Page,Doctor_Detail_Page,Blog_Detail_Page, Doctors_Page
from Users.views    import SignUp_Page,Login_Page,Log_Out_Page
from Admin_Control.views  import Your_Profile_Page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",                Home_page,           name="Home"),
    path("signup/",         SignUp_Page,         name="SignUp"),
    path("login/",          Login_Page,          name="Login"),
    path("logout/",         Log_Out_Page,        name="Logout"),
    path("your_profile/",   Your_Profile_Page,   name="Your_Profile"),
    path("contact/",        Contact_Page,        name="Contact_Us"),
    path("allservices/",    All_Services_Page,   name="All_Services"),
    path("service_detail/", Service_Detail_Page, name="Service_Detail"),
    path("blog/",           Blog_Page,           name="Blog"),
    path("doctors/",        Doctors_Page,        name="Doctors"),
    path("doctor_detail/",  Doctor_Detail_Page,  name="Doctor_Detail"),
    path("blog_detail/",    Blog_Detail_Page,    name="Blog_Detail"),
]
