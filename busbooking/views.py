
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.urls import reverse
from . models import needblood,donate


from . forms import donateform


# Create your views here.

def home(request):

    mydata=needblood.objects.all()
    if(mydata!=''):
        return render(request,'home.html',{'mydata':mydata})
    else:
        return render(request,'home.html') 
    
    
def msg(request):
    
    return render(request,'msg.html')
    


def pst(request):
     if request.method =='POST':
        Name =  request.POST['Name']    
        Mobile =  request.POST['Mobile'] 
        Area =  request.POST['Area'] 
        Type = request.POST['Type']   
        City = request.POST['City'] 
        obj=needblood()
        obj.Name=Name
        obj.Mobile=Mobile
        obj.Area=Area
        obj.Type=Type
        obj.City=City
        obj.save()
        mydata=needblood.objects.all()
        return HttpResponseRedirect(reverse('home'))
     else:
         
         return render(request,'pst.html')
  
    
def Register(request):
    if request.method =='POST':
        first_name =  request.POST['first_name']
        username =    request.POST['username']
        password =  request.POST['password']
        password2 =  request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
              messages.info(request,'username already exist')
              return redirect('register')
            else:
    
               user = User.objects.create_user(first_name=first_name,username=username,password=password,)
               user.save();
               print('user created')
               return redirect('/')
        else:
           messages.info(request,'password not matching')
           return redirect('register')
    else:
        
        return render(request,"registeration.html")

def login(request):
    if request.method =='POST':
        username= request.POST['username']
        password= request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is None:
            messages.info(request,'wrong crendtials')
            return redirect('/login')
        else:
            auth.login(request,user)
            return redirect('/')
    else:
     
      return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def donates(request):
    
    
    submitted = False
    if request.method =='POST':
        datas = donate.objects.all()
        
        form =  donateform(request.POST)
        if form.is_valid():
            form.save()
            return   redirect('/donate?submitted=True')  
    else:
        datas = donate.objects.all()
        form = donateform
        if 'submitted' in request.GET:
            submitted = True
        
    return render(request,'donate.html',{'form':form,'datas':datas,'submitted':submitted})
