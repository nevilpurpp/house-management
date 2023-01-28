from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import House


# Create your views here.


#new user registration
def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            messages.success(request, 'registration successful')
            return redirect('home')#home
        messages.error(request, 'Unsuccessful registration. Invalid information')
    form = NewUserForm()
    return render(request=request, template_name='home/register.html')

#login registration form
def login_request(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('home')#home
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request=request, template_name='home/login.html', context={'login_form':form})

#home
def home_request(request):
    return render(request, 'home/home.html')

#log out 
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('home')#home 

#House list
def house_list(request):
     houses = House.objects.all(available=True)

     return render(request,'home/house_list.html',{'houses':houses})


def house_detail(request, id, slug):
     house = get_object_or_404(House,
    id=id,slug=slug, available=True)
     return render(request,'home/detail.html',
     {'house': house})