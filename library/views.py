from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,'branches.html')

def sems(request):
	return render(request,'sems.html') 
