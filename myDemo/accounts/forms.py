from django.contrib.auth.forms import UserCreationForm
from .models import User  # Import User đã tùy chỉnh

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Model User tùy chỉnh
        fields = ('username', 'email', 'role')  # Các trường bạn muốn sử dụng
