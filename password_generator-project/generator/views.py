from django.shortcuts import render
import random

# Create your views here.
def home(request):
    if request.POST:
        character_str = 'abcdefghijklmnopqrstuvwxyz'
        characters = list(character_str)
        uppercase, special, numbers = False, False, False
        if request.POST.get('uppercase'):
            characters.extend(list(character_str.upper()))
            uppercase = True
        if request.POST.get('special'):
            characters.extend(list('!@#$%^&*()'))
            special = True
        if request.POST.get('numbers'):
            characters.extend(list('1234567890'))
            numbers = True

        length = int(request.POST.get('length', 12))
        thepassword = ''
        for x in range(length):
            thepassword += random.choice(characters)
        return render(request, 'generator/home.html', {'password':thepassword, 'uppercase':uppercase,
                                                       'special':special, 'numbers':numbers, 'length':length})
    else:
        return render(request, 'generator/home.html')

