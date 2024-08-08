from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def sign_up(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    else:
        form = SignUpForm()
    context={
        'form':form,
    }
    return render(request,'users/sign_up.html',context)

@login_required 
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST or None, instance=request.user) #here instance is to show the username
        profile_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)
        if user_form.is_valid() and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            return redirect('users-profile')

    else:
        user_form= UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profilemodel)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request,'users/profile.html',context)
