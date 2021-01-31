from django.urls import path
from . import views
#mục đích của Kteam là tạo đường dẫn /blog/id 
#để dựa vào id mà hiện thị đúng chi tiết bài viết. 
#Ở file urls.py của app blog cần khai báo path đó như sau:
urlpatterns = [
  path('', views.list,name='blog'),
  path('<int:id>/',views.post,name='post'),
]
