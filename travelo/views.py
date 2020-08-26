from django.shortcuts import render
from .models import myweb

# Create your views here.
def ind(request):
    nm1 = myweb()
    nm1.name='Harshit'
    nm1.image='bg_1.jpg'

    nm2 = myweb()
    nm2.name='Naman'
    nm2.image='bg_2.jpg'

    nm = [nm1, nm2]
    return render(request,'index.html',{'webname':nm})