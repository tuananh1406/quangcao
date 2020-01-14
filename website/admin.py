from django.db import models
from django.contrib import admin
from .models import BaiViet, Sanpham, Congty, Phongban, SanphamCon

# Register your models here.
class SanphamAdmin(admin.ModelAdmin):
    fieldsets = [
            ("Tên",
                {'fields': [ "sanpham_ten",]}
                ),
            ("Hình ảnh",
                {'fields': [ "sanpham_duongdan",]}
                ),
            ("Giá",
                {'fields': [ "sanpham_giatien",]}
                ),
            ]

class SanphamConAdmin(admin.ModelAdmin):
    fieldsets = [
            ("Tên",
                {'fields': [ "sanpham_ten",]}
                ),
            ("Hình ảnh",
                {'fields': [ "sanpham_duongdan",]}
                ),
            ("Giá",
                {'fields': [ "sanpham_giatien",]}
                ),
            ]

class BaiVietAdmin(admin.ModelAdmin):
    fieldsets = [
            ("Tiêu đề/Thời gian",
                {'fields': [
                    "baiviet_tieude",
                    "baiviet_ngaydang",
                    ]}),
            ("Nội dung",
                {'fields': [
                    "baiviet_noidung",
                    "baiviet_sanpham",
                    ]})
    ]

class CongtyAdmin(admin.ModelAdmin):
    fieldsets = [
            ("Tên công ty",
                {'fields': [ "congty_ten",]}
                ),
            ("Điện thoại",
                {'fields': ["congty_dienthoai"]}
                ),
            ("Hotline",
                {'fields': ["congty_hotline"]}
                ),
            ("Địa chỉ",
                {'fields': ["congty_diachi"]}
                ),
            ("Xưởng sản xuất",
                {'fields': ["congty_xuongsanxuat"]}
                ),
            ("Logo",
                {'fields': ["congty_logo"]}
                ),
            ]

class PhongbanAdmin(admin.ModelAdmin):
    fieldsets = [
            ("Tên phòng ban",
                {'fields': ['tenphong']}
                ),
            ('Số điện thoại',
                {'fields': ['sodienthoai']}
                ),
            ]

admin.site.register(SanphamCon)
admin.site.register(BaiViet, BaiVietAdmin)
admin.site.register(Sanpham)
admin.site.register(Phongban)
admin.site.register(Congty)
