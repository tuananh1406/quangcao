from django.db import models
from datetime import datetime

# Create your models here.
class BaiViet(models.Model):
    baiviet_tieude = models.CharField('Tiêu đề', max_length=200)
    baiviet_noidung = models.TextField('Nội dung',
            )
    baiviet_noidung_rutgon = models.TextField('Nội dung rút gọn')
    baiviet_ngaydang = models.DateTimeField('Ngày đăng bài',
            default=datetime.now)

    def __str__(self):
        return self.baiviet_tieude

class Sanpham(models.Model):
    sanpham_id = models.AutoField(primary_key=True)
    sanpham_ten = models.CharField('Tên sản phẩm', max_length=200)
    sanpham_hinhanh = models.ImageField('Đường dẫn hình ảnh',
            upload_to='anhsanpham/')
    sanpham_giatien = models.CharField('Giá tiền', max_length=50)

    def __str__(self):
        return self.sanpham_ten

class Congty(models.Model):
    congty_ten = models.CharField('Tên công ty', max_length=500)
    congty_dienthoai = models.CharField('Điện thoại', max_length=15)
    congty_hotline = models.CharField('Hotline', max_length=15)
    congty_email = models.CharField('Email', max_length=50)
    congty_diachi = models.CharField('Địa chỉ', max_length=1000)
    congty_xuongsanxuat = models.CharField('Xưởng sản xuất', max_length=1000)
    congty_logo = models.ImageField('Logo', upload_to='logo_congty')

    def __str__(self):
        return self.congty_ten

class Phongban(models.Model):
    tenphong = models.CharField('Tên phòng', max_length=100)
    sodienthoai = models.CharField('Số điện thoại', max_length=15)

    def __str__(self):
        return self.tenphong
