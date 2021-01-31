from django.shortcuts import render
# Create your views here.
#Truy vấn lấy bài viết và chuyển qua template
#Bước 1: ta sẽ import model Post để có thể truy vấn dữ liệu.
#Bước 2: tạo hàm list để xử lý request yêu cầu liệt kê bài viết
#Bước 3: tạo một biến Data kiểu dict, có key là Posts với value là câu truy vấn lấy toàn bộ bài viết và nó được sắp xếp bằng date, việc thêm dấu trừ là sắp xếp từ bài mới nhất đến bài cũ nhất
#Bước 4: render sang template blog.html, đưa Data vào tham số cuối để template dùng dữ liệu để tạo giao diện
from .models import Post
def list (request):
    Data ={'Posts' : Post.objects.all().order_by('-date')}
    return render (request,'blog/blog.html',Data)
#Bây giờ, ta sẽ viết hàm post để xử lý path trên: 
#ta còn thêm tham số id tương ứng keyword id ở path. Sau đó, ta sẽ truy vấn bài viết bằng id trên. Rồi đưa bài viết vào render, bây giờ kteam sẽ   
def post (request,id):
    post=Post.objects.get(id=id)
    return render (request,'blog/post.html',{'post':post})
    
