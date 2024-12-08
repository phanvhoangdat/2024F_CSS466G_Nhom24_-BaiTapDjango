from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Xác thực người dùng
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Đăng nhập thành công
            login(request, user)
            messages.success(request, 'Đăng nhập thành công!')
            return redirect('home')  # Chuyển hướng về trang chủ hoặc trang khác
        else:
            # Đăng nhập thất bại
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không chính xác.')

    # Hiển thị form đăng nhập
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Lưu người dùng và đăng nhập ngay lập tức
            user = form.save()
            login(request, user)
            messages.success(request, 'Tài khoản của bạn đã được tạo thành công!')
            return redirect('home')  # Chuyển hướng về trang chủ hoặc trang khác
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin đăng ký.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})