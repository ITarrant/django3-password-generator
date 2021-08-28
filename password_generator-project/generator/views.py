from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    character_str = 'abcdefghijklmnopqrstuvwxyz'
    characters = list(character_str)

    if request.GET.get('uppercase'):
        characters.extend(list(character_str.upper()))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})