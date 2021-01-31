from django.test import TestCase
from .models import Post
# Create your tests here.
#Phương thức setUp đầu tiên là tạo 1 bài 
#viết trong hệ thống test, bài viết được tạo ở đây
#sẽ không ảnh hưởng gì đến database đang làm.
class BlogTest(TestCase):
    def setUp(self):
        Post.objects.create(
            title='myTitle',
            body='just a Test'
        )
#Phương thức test_string_representation nhằm để kiểm tra phương thức __str__ của Post có ra giá trị title không. Kteam tạo ra 1 post và so sánh hai giá trị dùng hàm gán str() và gọi tiêu đề title ra.        
    def test_string_representation(self):
        post = Post(title='Post object (None)')
        self.assertEqual(str(post), post.title)
#Phương thức test_post_list_view kiểm tra chức năng hiển thị danh sách bài viết, bằng cách vào đường dẫn /blog/ kiểm tra status code có trả về 200 không? Trong response có tiêu đề bài viết không? Có sử dụng template blog.html như đã làm không.
    def test_post_list_view(self):
       response=self.client.get('/blog/')
       self.assertEqual(response.status_code,200)
       self.assertContains(response,'myTitle')
       self.assertTemplateUsed(response, 'blog/blog.html')
#Phương thức test_post_detail_view kiểm tra chức năng hiển thị thông tin bài viết, cách kiểm tra cũng tương tự hiển thị danh sách bài viết.
    def test_post_detail_view(self):
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'myTitle')
        self.assertTemplateUsed(response, 'blog/post.html')
#python manage.py test blog