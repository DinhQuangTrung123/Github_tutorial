from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   return render(request,'pages/home.html')
   #Ta sẽ gọi template bằng hàm render,
   # hàm render có 2 tham số truyền vào: đầu tiên là request là
   # request từ máy client, thứ 2 là tên đường dẫn đến template ta
   # muốn dùng (ta chỉ cần gọi đường dẫn bên trong folder 'templates')
def contact(request):
   return render(request,'pages/contact.html')
def blog(request):
   return render(request,'pages/blog.html')

