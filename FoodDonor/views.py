from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserInfoForm

def home(request):
    return render(request,"home.html") 
def about(request):
    return render(request,'about.html')
def register(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'success.html') # Redirect to login page after successful registration
    else:
        form = UserInfoForm
    return render(request, 'register.html', {'form': form})