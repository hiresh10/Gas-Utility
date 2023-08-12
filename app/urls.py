from django.urls import path
from .import views

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("signuppage/",views.SignUppage,name="signuppage"),
    path("register/",views.Register,name="register"),
    path("login/",views.Login,name="login"),
    path("home/",views.Homepage,name="home"),
    path("profilepage/",views.UserProfile,name="profilepage"),
    path('updateprofile/<int:pk>', views.update_profile, name='update_profile'),
    path("submitpage/",views.RequestPage,name="requestpage"),
    path("submit_request/<int:pk>",views.SubmitRequest,name="submitrequest"),
    path("requests/",views.Requests,name="requests"),
    path("Logout/",views.Logout,name="logout"),
#####################  ADMIN URLS   #############################

    path("adminloginpage/",views.AdminLoginPage,name="adminloginpage"),
    path("adminlogin/",views.Aminlogin,name="adminlogin"),
    path("userlistpage/",views.UserList,name="userlist"),
    path("userdelete/<int:pk>",views.UserDelete,name="user_delete"),
    path("requests/",views.AdminRequests,name="requests"),
    path("resoponse/<int:request_id>",views.SendResponse,name="response"),
    path("servicedelete/<int:pk>",views.RequestDelete,name="service_delete"),
    path("adminlogout/",views.Adminlogout,name="adminlogout"),
]