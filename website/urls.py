from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [
        path('', views.trangchu, name="trangchu"),
        #path('dangky/', views.dangky, name="dangky"),
        path('dangnhap/', views.dangnhap, name="dangnhap"),
        path('dangxuat/', views.dangxuat, name="dangxuat"),
        path('themsanpham/', views.themsanpham, name="themsanpham"),
        path('themsanphamcon/', views.themsanphamcon, name="themsanphamcon"),
        path('thembaiviet/', views.thembaiviet, name="thembaiviet"),
        path('xembaiviet/', views.xembaiviet, name="xembaiviet"),
        path('gioithieu/', views.gioithieu, name="gioithieu"),
        path('<duongdan>', views.duongdanrutgon, name="duongdanrutgon"),
]
