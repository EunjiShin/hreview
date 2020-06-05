
from django.contrib import admin
from django.urls import path, include
import hyuzi.views
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

User = get_user_model()

# UserCreationForm이라는 기존의 유저생성폼을 상속받아 필요한 필드만 사용할 수 있도록 구현. 
# 이후 필요한 필드로 수정
class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'nickname', 'username', 'email', 'address', 'phone', 'password1', 'password2'}

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = {'nickname', 'email', 'address', 'phone'}


# 회원가입 구현
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

# 유저 정보 수정
@login_required
def user_update(request):
    if request.method == 'POST':
        user_change_form = UserChangeForm(data=request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('mypage')
    else:
        user_change_form = UserChangeForm(instance=request.user)
    return render(request, 'registration/user_update.html', {'user_change_form':user_change_form})

# 비밀번호 수정
@login_required
def change_password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            return redirect('main')
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'password_change_form' : password_change_form})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hyuzi/', include('hyuzi.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('user_update/', user_update, name='user_update'),
    path('change_password/', change_password, name='change_password'),
]  

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)