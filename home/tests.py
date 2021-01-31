#tạo ra test case
from django.test import TestCase,SimpleTestCase
# Create your tests here.
# kiểm tra hàm index trong views
class SimpleTest(SimpleTestCase):
    def test_home_page_status(self):
        response =self.client.get('/')
        self.assertEquals(response.status_code,200)#trang thành công nó trả vè 200 còn không thành công nó trả về 404