from django.shortcuts import render
import requests
from .models import Link
from bs4 import BeautifulSoup
# Create your views here.


def scrap(request):
    page=requests.get('https://www.google.com')
    soup=BeautifulSoup(page.text,'html.parser')
    
    for link in soup.find_all('a'):
        link_address=link.get('href')
        link_text=link.string
        Link.objects.create(address=link_address,name=link_text)

    data=Link.objects.all()
    return render(request,'myapp/results.html',{'data':data})