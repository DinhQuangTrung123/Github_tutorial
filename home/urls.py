from django.urls import path
from . import views # dấu chấm được hiểu như là đường dẫn nó nằm chng trong 1 thư mục 


urlpatterns = [
    path('',views.index),
    path('contact/',views.contact,name='contact'),
]