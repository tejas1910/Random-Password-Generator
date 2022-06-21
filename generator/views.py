from django.forms import PasswordInput
from django.shortcuts import render
import random
from django.http import HttpResponse

# Create your views here.
 
def home(request):
    return render(request,'generator/home.html')
    # return HttpResponse('blabla')

def password(request):
    thepassword = "testing"
    characters=list('abcdefghijklmnpqrstuvwxyz')

    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('Special Characters'):
        characters.extend(list('!@#$%^&*()_+=-'))
    
    if request.GET.get('Numbers'):
        characters.extend(list('1234567890'))

    length= int(request.GET.get('length'))

    thepassword=''
    for x in range(length):
        thepassword+= random.choice(characters)
    return render(request,'generator/password.html', {'password':thepassword})
