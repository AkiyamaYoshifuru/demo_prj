from django.shortcuts import redirect, render
from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

# 初始欢迎页面：有个小笑脸😊的那个，提供登陆和注册新账号的功能按钮 & DFT联系方式
def home(request):
    '''已登陆后的重定向'''
    # if request.user.is_authenticated:
    #     if request.user.is_operator:
    #         return redirect('operators:quiz_change_list')
    #     else:
    #         return redirect('officers:quiz_list')
    return render(request, 'core/home.html')

def dashboard(request):
    return render(request, 'db0/dashboard.html')

def tables(request):
    return render(request, 'db0/data_tables.html')

def statics(request):
    return render(request, 'db0/statistical_chart.html')

def settings(request):
    return render(request, 'db0/device_setting.html')

def valueInputSetting(request):
    return render(request, 'db0/value_limit_input.html')

def upload(request):
    return render(request, 'db0/upload_status.html')