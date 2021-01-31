from django.db import models
#có ba trường dữ liệu
#title: lưu tiêu đề bài viết, có đồ dài tối đa là 100 kí tự
#body: nội dung bài viết, không giới hạn kí tự
#date: ngày viết bài, tự thêm ngày hiện tại khi tạo ra bài viết
# Create your models here.
#Khai báo class Post kế thừa models.Model, là class được viết ra ánh xạ đến bảng trong Database.
#Khai báo field title ánh xạ đến cột title trong bảng. Field title sẽ thuộc CharField có tham số max_length=100, có nghĩa cột title sẽ lưu trữ kiểu String và dài nhất 100 ký tự.
#Khai báo field body ánh xạ đến cột body trong bảng. Field body sẽ thuộc TextField, có nghĩa cột body lưu trữ kiểu String vài không giới hạn độ dài
#Khai báo field  date ánh xạ đến cột date trong bảng. Field date sẽ có thuộc tính DateTimeField có tham số auto_now_add=True, có nghĩa cột date lưu kiểu Date và tự động thêm ngày hiện tại cho record mới.
#python manage.py makemigrations blog tạo cái này đề migration biết đã tạo ra một class post
class Post(models.Model):
    objects = models.Manager()
    title =models.CharField(max_length=100)
    body= models.TextField()
    date =models.DateTimeField(auto_now_add=True)
#ta override lại phương thức đề in ra dễ hiểu hơn
def __str__(self):
    return self.title

#from blog.models import Post
#Post.objects.all()
#Post.objects.get(id=1)
#a = Post.objects.get(id=1)
#a.body = 'Hello Kteam'
#a.save()