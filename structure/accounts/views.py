from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout

from structure.accounts.models.base import User
from structure.accounts.models.profile import Profile

class LoginView(View):
    
    def get(self,request):
        return render(request,'user/login.html')

    def post(self,request):
        # getting data from client 
        username = request.POST.get('username',None)
        password =request.POST.get('password',None)

        match_user = User.objects.filter(
            Q(username=username) |
            Q(profile__phone=username)
        )
        if match_user.exists():
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                # message
                return redirect('login')
        else:
            # message
            return redirect('login')
            



        



class RegisterView(View):

    def get(self,request):
        return render(request,'user/sign-up.html')

    def post(self,request):
        # getting data from client 
        full_name = request.POST.get('fullname',None)
        phone_number = request.POST.get('phone',None)
        password = request.POST.get('password1',None)
        confirm_password = request.POST.get('password2',None)


        create_user = User(
            username = f"{full_name}##{phone_number}",
            password = make_password(password),
            confirm_password = make_password(confirm_password)
        )
        create_user.save()

        save_profile = Profile(
            user = create_user,
            full_name = full_name,
            phone = phone_number
        )
        save_profile.save()




class CheckPhoneNumber(View):
    def post(self,request):
        phone_number = request.POST.get('phone')
        
        if Profile.objects.filter(phone=phone_number).exists():
            return HttpResponse("The Phone Number Already Exists !")
        else:
            return HttpResponse("The Phone Number is Available")
            


class CheckPassword(View):
    def post(self,request):
        # getting password
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password != confirm_password:
            return HttpResponse("Password & Confirm Password Mismatch")
        else:
            return HttpResponse("Password Match ! WOW")
