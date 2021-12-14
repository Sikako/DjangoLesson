# from django.http import HttpResponse
from django.shortcuts import render

# def Hello(request):
  # return HttpResponse("Hello World")
def index(request):
  context = {}
  context["name"] = "Sikako"
  return render(request,"index.html",context)