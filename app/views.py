from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def IndexPage(request):
    return render(request, 'app/index.html')


def LoginPage(request):
    return render(request,'app/login.html')


def SignUppage(request):
    return render(request,'app/signup.html')


def Register(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email).exists()
        
        if user:
            message = "User Already Exists"
            return render(request,'app/signup.html',{'msg':message})
        else:
            if (password == cpassword):
                newuser = UserMaster.objects.create(email=email, password=password)

                message = "Regitration Successfull"
                return render(request, 'app/login.html', {'msg':message})
            else:
                message="Password and Confirm Password does not match!"
                return render(request,'app/signup.html',{'msg':message})
            
    else:
        return render(request,'app/signup.html')
    

    

def Login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserMaster.objects.get(email=email)
            if user.password == password:
                request.session['id'] = user.id
                request.session['email'] = user.email
                request.session['password'] = user.password
                message = "Login Successful!"
                return render(request, 'app/home.html', {'msg': message})
            else:
                e_message = "Incorrect Password"
                return render(request, 'app/login.html', {'emsg': e_message})
        except ObjectDoesNotExist:
            e_message = "User does not exist"
            return render(request, 'app/login.html', {'emsg': e_message})
    else:
        e_message = "Bad Request"
        return render(request, 'app/login.html', {'emsg':e_message})
    


def Homepage(request):
    return render(request,'app/home.html')



def UserProfile(request):
    return render(request,'app/profile.html')



def update_profile(request, pk):
    user = get_object_or_404(UserMaster, pk=pk)

    if request.method == 'POST':
        customer = get_object_or_404(Customer, custermer_id=user)

        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')

        if name:
            customer.name = name
            user.name = name
        
        if contact:
            customer.contact = contact
            user.contact = contact
        
        if address:
            customer.address = address
            user.address = address

        customer.save()
        user.save()

        message = "Profile updated successfully"
        return render(request, 'app/profile.html', {'user': user, 'msg': message})

    return render(request, 'app/profile.html', {'user': user})



def Requests(request):
    all_requests = ServiceRequest.objects.all()
    return render(request,'app/servicerequest.html',{'all_requests':all_requests})



def RequestPage(request):
    return render(request,'app/create_request.html')



def SubmitRequest(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user:
        username = user.email
        request_type = request.POST.get('request_type')  
        request_details = request.POST.get('request_details') 
        request_file = request.FILES.get('request_file')

        new_request = ServiceRequest.objects.create(
                    usermasterid = user,
                    username = username,
                    request_type=request_type,
                    request_detail=request_details,
                    request_file=request_file
                )
        message = "Request Submitted Successfully"

        return render(request,'app/create_request.html',{'msg':message})
    else :
        e_message = "User Does Not Exists!!"
        return render(request,'app/create_request.html',{'msg':message})
    

    
def Logout(request):
    del request.session['email']
    del request.session['password']
    return redirect('index')


####################################   ADMIN VIEW    ########################################



def AdminLoginPage(request):
    return render(request,'admin/adminlogin.html')



def Aminlogin(request):
    username = request.POST['username']
    password = request.POST['password']

    if username == "admin" and password == "admin":

        request.session['username'] = username
        request.session['password'] = password
        message = "Welcome ADMIN"
        return render(request,'admin/adminhome.html')

    else:
        message = "Username and password not match"
        return render(request,"admin/adminlogin.html",{'msg':message})
    

    
def UserList(request):
    all_users = UserMaster.objects.all()
    return render(request,'admin/userlist.html',{'all_users':all_users})


    
def UserDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('userlist')




def AdminRequests(request):
    all_requests = ServiceRequest.objects.all()
    return render(request,'admin/adminhome.html',{'all_requests':all_requests})


    
def SendResponse(request, request_id):
    if request.method == "POST":
        resolution_date = request.POST.get("resolution_date")
        
        # Retrieve the existing ServiceRequest object
        service_request = get_object_or_404(ServiceRequest, id=request_id)

        # Update the resolution_date and save the object
        service_request.resolution_date = resolution_date
        service_request.save()

        message = "Date Updated successfully!"
        return render(request, 'admin/adminhome.html', {'msg': message})



def RequestDelete(request,pk):
    service = ServiceRequest.objects.get(pk=pk)
    service.delete()
    return redirect('userlist')


    
def Adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('index')

# 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