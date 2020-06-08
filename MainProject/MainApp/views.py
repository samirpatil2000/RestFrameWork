from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

from.forms import UserRegisterForm



def home(request):
    return render(request,'MainApp/home.html')

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Has Been Created {username} !')
            return redirect('login')
    else:
        form=UserRegisterForm()

    return render(request,'MainApp/register.html',{'form':form})