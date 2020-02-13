from django import forms
from .models import Sanpham, BaiViet
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class FormSanpham(forms.Form):
    ten = forms.CharField(
            label="Tên sản phẩm",
            max_length=100,
            )
    hinhanh = forms.ImageField(
            label="Hình ảnh",
            )
    giatien = forms.CharField(
            label="Giá tiền",
            max_length=100,
            )

class FormSanphamCon(forms.Form):
    ten = forms.CharField(
            label="Tên sản phẩm",
            max_length=100,
            )
    hinhanh = forms.ImageField(
            label="Hình ảnh",
            )
    giatien = forms.CharField(
            label="Giá tiền",
            max_length=100,
            )
    dssanpham = Sanpham.objects.all()
    dsluachon = [
            (sanpham.sanpham_id, sanpham.sanpham_ten)
            for sanpham in dssanpham
            ]
    sanphamcha = forms.ChoiceField(label="Sản phẩm", choices=dsluachon)

class FormBaiViet(forms.Form):
    tieude = forms.CharField(
            label="Tiêu đề",
            max_length=100,
            )
    hinhanh = forms.ImageField(
            label="Ảnh bìa",
            )
    noidung = forms.CharField(
            label="Nội dung",
            widget=CKEditorUploadingWidget,
            )
    noidung_rutgon = forms.CharField(
            label="Nội dung rút gọn",
            widget=CKEditorUploadingWidget,
            )
    dssanpham = Sanpham.objects.all()
    dsluachon = [
            (sanpham.sanpham_id, sanpham.sanpham_ten)
            for sanpham in dssanpham
            ]
    sanpham = forms.ChoiceField(label="Sản phẩm", choices=dsluachon)

class FormSuaSanPham(forms.ModelForm):
    class Meta:
        model = Sanpham
        fields = [
                'sanpham_ten',
                'sanpham_hinhanh',
                'sanpham_giatien',
                ]

class FormSuaBaiViet(forms.ModelForm):
    baiviet_noidung = forms.CharField(
            label="Nội dung",
            widget=CKEditorUploadingWidget,
            )
    baiviet_noidung_rutgon = forms.CharField(
            label="Nội dung rút gọn",
            widget=CKEditorUploadingWidget,
            )
    dssanpham = Sanpham.objects.all()
    dsluachon = [
            (sanpham.sanpham_id, sanpham.sanpham_ten)
            for sanpham in dssanpham
            ]
    baiviet_sanpham_id = forms.ChoiceField(label="Sản phẩm", choices=dsluachon)
    class Meta:
        model = BaiViet
        fields = [
                'baiviet_tieude',
                'baiviet_hinhanh',
                'baiviet_noidung',
                'baiviet_noidung_rutgon',
                'baiviet_sanpham_id',
                ]
