from django import forms
from .models import Sanpham, BaiViet
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class FormSanpham(forms.ModelForm):
    class Meta:
        model = Sanpham
        fields = ('sanpham_ten', 'sanpham_hinhanh', 'sanpham_giatien')

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
