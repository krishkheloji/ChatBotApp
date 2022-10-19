from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .forms import ChatForm
from .models import ChatModel
# Create your views here.

def home(request):
    return render(request,'base.html')

class Chat(View):
    def get(self,request):
        form=ChatForm()
        users=ChatModel.objects.all()
        d={'users':users,'form':form}
        return render(request,'chat.html',d)
        

    def post(self,request):
        muser=request.user
        message=request.POST['msg']
        cm=ChatModel(user=muser,msg=message)
        cm.save()
        return redirect('chat')

class Login(View):  
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        username=request.POST['User']
        password=request.POST['Pass']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('chat')
        else:
            return redirect('login')

def logout(request):
    auth_logout(request)
    return redirect('/')