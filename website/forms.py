from django import forms
from .models import Sanpham, BaiViet
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class FormSanpham(forms.ModelForm):
    class Meta:
        model = Sanpham
        fields = ('sanpham_ten', 'sanpham_hinhanh', 'sanpham_giatien')

class FormBaiViet(forms.ModelForm):
    content = forms.CharField(
            label="Nội dung",
            widget=CKEditorUploadingWidget,
            )
    class Meta:
        model = BaiViet
        fields = (
                'baiviet_tieude',
                'baiviet_noidung',
                'baiviet_noidung_rutgon',
                )
