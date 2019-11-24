from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import Sanpham,BaiViet, Congty, Phongban
from .forms import FormSanpham, FormBaiViet
from .xuly import taoslug, kiemtraslug

# Create your views here.
def lay_sanpham():
    #Lấy danh sách sản phẩm
    ds_sanpham = Sanpham.objects.all()
    danhsach = [ ["#", sanpham.sanpham_ten ] for sanpham in ds_sanpham ]
    return danhsach

def lay_sanpham_chitiet():
    #Lấy chi tiết sản phẩm
    danhsach = Sanpham.objects.all()
    danhsach_sanpham = [["#",
            sanpham.sanpham_ten,
            sanpham.sanpham_hinhanh.url,
            sanpham.sanpham_giatien,
            ] for sanpham in danhsach ]
    danhsach_sanpham_hang = []
    for i in range(0, len(danhsach_sanpham), 4):
        danhsach_sanpham_hang.append(danhsach_sanpham[i:i+4])
    return danhsach_sanpham_hang

def thongtin_trangchu():
    #Danh sách sản phẩm
    danhsach_sanpham = lay_sanpham()

    #Danh mục trên
    danhmuc = [
        [reverse("website:trangchu"), "trang chủ", None],
        ["#", "giới thiệu", None],
        [reverse("website:xembaiviet"), "sản phẩm",
            {
                "id": 18,
                "dulieu": danhsach_sanpham,
                }
            ],
        ["#", "dự án mới", None],
        ["#", "khuyến mãi", None],
        ["#", "khách hàng", None],
        ]

    #Danh sách mạng xã hội
    links = [
            ["hinhanh/f.png", "#", "Facebook"],
            ["hinhanh/z.png", "#", "Zing me"],
            ["hinhanh/g.png", "#", "Google plus"],
            ["hinhanh/b.png", "#", "Blogger"],
            ["hinhanh/t.png", "#", "Twitter"],
            ["hinhanh/r.png", "#", "RSS"],
            ]

    #Slide trình chiếu
    trinhchieu = [
            {
                "duongdan": "/static/hinhanh/bienhopden.jpg",
                "tieude": "Biển hộp đèn",
                },
            {
                "duongdan": "/static/hinhanh/bienhopden1.jpg",
                "tieude": "Biển hộp đèn",
                },
            {
                "duongdan": "/static/hinhanh/bienopcot.jpg",
                "tieude": "Biển hộp đèn",
                },
            {
                "duongdan": "/static/hinhanh/bienhethong.jpg",
                "tieude": "Biển hộp đèn",
                },
            ]

    #Quản trị viên
    quantri = [
            [reverse('website:themsanpham'), 'Thêm sản phẩm'],
            #[reverse('website:xemsanpham'), 'Xem sản phẩm'],
            [reverse('website:thembaiviet'), 'Thêm bài viết'],
            [reverse('website:xembaiviet'), 'Xem bài viết'],
            ]

    #Thông tin công ty
    congty = Congty.objects.all()[0]

    #Phòng ban
    phongban = Phongban.objects.all()

    #Tạo nội dung trang chủ
    context_trangchu = {
        "danhmuc": danhmuc,
        "links": links,
        "trinhchieu": trinhchieu,
        "danhsach_sanpham": danhsach_sanpham,
        "congty": congty,
        "phongban": phongban,
        }
    return context_trangchu

def trangchu(request):
    context = thongtin_trangchu()
    context['hang_sanpham'] = lay_sanpham_chitiet()
    return render(
            request = request,
            template_name = 'website/giaodien.html',
            context = context,
            )

def dangnhap(request):
    if request.user.is_authenticated:
        return redirect("website:trangchu")
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                    username=username,
                    password=password,
                    )
            if user is not None:
                login(request, user)
                messages.info(request,
                        "Bạn đã đăng nhập bằng tên {username}",
                        )
                return redirect('/')
            else:
                messages.error(request, "Sai tên tài khoản và mật khẩu")
        else:
            messages.error(request, "Sai tên tài khoản và mật khẩu")
    context = thongtin_trangchu()
    form = AuthenticationForm()
    context['form'] = form
    return render(
            request = request,
            template_name = 'website/dangnhap.html',
            context = context,
            )

def themsanpham(request):
    if not request.user.is_authenticated:
        return redirect("website:dangnhap")
    if request.method == "POST":
        form = FormSanpham(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/themsanpham')
    else:
        form = FormSanpham()
    context = thongtin_trangchu()
    context['form'] = form
    return render(
            request = request,
            template_name = "website/themsanpham.html",
            context = context,
            )

def thembaiviet(request):
    if not request.user.is_authenticated:
        return redirect("website:dangnhap")
    if request.method == "POST":
        form = FormBaiViet(request.POST, request.FILES)
        if form.is_valid():
            baiviet = BaiViet()
            baiviet.baiviet_tieude = form.cleaned_data['tieude']
            baiviet.baiviet_hinhanh = form.cleaned_data['hinhanh']
            baiviet.baiviet_noidung = form.cleaned_data['noidung']
            baiviet.baiviet_noidung_rutgon = form.cleaned_data['noidung_rutgon']
            ds_slug = [ cacbaiviet.baiviet_slug for cacbaiviet in BaiViet.objects.all() ]
            slug = taoslug(baiviet.baiviet_tieude).lower()
            baiviet.baiviet_slug = kiemtraslug(ds_slug, slug)
            id_sanpham = form.cleaned_data['sanpham']
            baiviet.baiviet_sanpham = Sanpham.objects.get(sanpham_id=id_sanpham)
            baiviet.save()
            return redirect('website:xembaiviet')
    else:
        form = FormBaiViet()
    context = thongtin_trangchu()
    context['form'] = form
    return render(
            request = request,
            template_name = 'website/thembaiviet.html',
            context = context,
            )

def xembaiviet(request):
    context = thongtin_trangchu()
    context['dsbaiviet'] = BaiViet.objects.all()
    return render(
            request=request,
            template_name = 'website/xembaiviet.html',
            context=context,
            )

def duongdanrutgon(request, duongdan):
    ds_baiviet = [baiviet.baiviet_slug for baiviet in BaiViet.objects.all()]
    ds_sanpham = [sanpham.sanpham_slug for sanpham in Sanpham.objects.all()]
    if duongdan in ds_baiviet:
        return HttpResponse("%s bài viết" % (duongdan))
    return HttpResponse("%s không tìm thấy" % (duongdan))

    if duongdan in ds_sanpham:
        return HttpResponse("%s bài viết" % (duongdan))
    return HttpResponse("%s không tìm thấy" % (duongdan))

def dangxuat(request):
    logout(request)
    return redirect("website:trangchu")
