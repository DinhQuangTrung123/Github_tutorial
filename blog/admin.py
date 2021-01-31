from django.contrib import admin

# Register your models here.
#Bây giờ Kteam muốn hệ thống Admin có thể quản lý 
#model Post từ bài trước. Đầu tiên là vào file admin.py trong app blog. 
#Import model Post qua và register vào bằng dòng code dưới đây.
from .models import Post
# Register your models here.
#để hiển thị thời gian ta cần làm
#Tiếp theo, Kteam muốn tạo filter để lọc bài viết, Kteam sẽ lọc bài viết theo ngày viết bài thì tạo thêm một list là  list_filter chứa giá trị date tương ứng field của bảng Post:
#search theo title
class PostAdmin (admin.ModelAdmin):
    list_display =['title','body','date']
    list_filter=['date']
    search_fields=['title']
admin.site.register(Post,PostAdmin)