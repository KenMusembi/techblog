from django.http import HttpResponse
from django.shortcuts import render

#function for home page
def home(request):
    # return HttpResponse()
    return render(request, 'home.html')

#function to take us to the abouts page
def about(request):
    return render(request, 'about.html')
