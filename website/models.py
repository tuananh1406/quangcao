from django.db import models
from datetime import datetime

# Create your models here.
class Sanpham(models.Model):
    sanpham_id = models.AutoField(primary_key=True)
    sanpham_ten = models.CharField('Tên sản phẩm', max_length=200)
    sanpham_hinhanh = models.ImageField('Đường dẫn hình ảnh',
            upload_to='anhsanpham/')
    sanpham_giatien = models.CharField('Giá tiền', max_length=50)
    sanpham_slug = models.SlugField(
            'Đường dẫn rút gọn',
            default=1,
            )

    class Meta:
        verbose_name_plural = "Sản phẩm"

    def __str__(self):
        return self.sanpham_ten

class SanphamCon(models.Model):
    sanpham_id = models.AutoField(primary_key=True)
    sanpham_ten = models.CharField('Tên sản phẩm', max_length=200)
    sanpham_hinhanh = models.ImageField('Đường dẫn hình ảnh',
            upload_to='anhsanpham/')
    sanpham_giatien = models.CharField('Giá tiền', max_length=50)
    sanpham_slug = models.SlugField(
            'Đường dẫn rút gọn',
            default=1,
            )
    sanpham_sanphamcha = models.ForeignKey(
            Sanpham,
            default=3,
            verbose_name="Sản phẩm",
            on_delete=models.SET_DEFAULT,
            )

    class Meta:
        verbose_name_plural = "Sản phẩm con"

    def __str__(self):
        return self.sanpham_ten

class BaiViet(models.Model):
    baiviet_tieude = models.CharField('Tiêu đề', max_length=200)
    baiviet_hinhanh = models.ImageField('Ảnh bìa',
            upload_to='anhbia/')
    baiviet_noidung = models.TextField('Nội dung')
    baiviet_noidung_rutgon = models.TextField('Nội dung rút gọn')
    baiviet_slug = models.SlugField(
            'Đường dẫn rút gọn',
            default=1,
            )
    baiviet_sanpham = models.ForeignKey(
            Sanpham,
            default=3,
            verbose_name="Sản phẩm",
            on_delete=models.SET_DEFAULT,
            )
    baiviet_ngaydang = models.DateTimeField('Ngày đăng bài',
            default=datetime.now)

    class Meta:
        verbose_name_plural = "Bài viết"

    def __str__(self):
        return self.baiviet_tieude

class Congty(models.Model):
    congty_ten = models.CharField('Tên công ty', max_length=500)
    congty_dienthoai = models.CharField('Điện thoại', max_length=15)
    congty_hotline = models.CharField('Hotline', max_length=15)
    congty_email = models.CharField('Email', max_length=50)
    congty_diachi = models.CharField('Địa chỉ', max_length=1000)
    congty_xuongsanxuat = models.CharField('Xưởng sản xuất', max_length=1000)
    congty_logo = models.ImageField('Logo', upload_to='logo_congty')
    congty_banner = models.ImageField('Banner', upload_to='banner',
            default='banner/top_banner.png')

    class Meta:
        verbose_name_plural = "Công ty"

    def __str__(self):
        return self.congty_ten

class Phongban(models.Model):
    tenphong = models.CharField('Tên phòng', max_length=100)
    sodienthoai = models.CharField('Số điện thoại', max_length=15)
    chucvu = models.CharField('Chức vụ', max_length=50)

    class Meta:
        verbose_name_plural = "Phòng ban"

    def __str__(self):
        return self.tenphong
