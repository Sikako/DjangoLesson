# from django.http import HttpResponse
from django.shortcuts import render

# def Hello(request):
  # return HttpResponse("Hello World")

# index被呼叫就回傳templates中的index.html並使用context去填充變量
def index(request):
  context = {}
  context["name"] = "Sikako"
  return render(request,"index.html",context)