from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import AccountRegisterForm,AccountUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            messages.success(request,f'Account created for {username}! You are now able to log in.')
            return redirect('login')
    else:
        form = AccountRegisterForm()
    return render(request,'accounts/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        account_form = AccountUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if account_form.is_valid() and profile_form.is_valid():
            account_form.save()
            profile_form.save()
            messages.success(request,f'Your account has been updated')
            return redirect('profile')
    else:
        account_form = AccountUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context= {
        'account_form':account_form,
        'profile_form':profile_form
    }
    return render(request,'accounts/profile.html',context)