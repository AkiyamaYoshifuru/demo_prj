from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
# 使用自定义的login View，便于跳转页面
# from . import login
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from ..forms import OperatorSignUpForm
from ..decorators import operator_required
from ..models import User
from ..templatetags import dict_key

# 不能是def一个方法，需要定义一个类
class DftStaffSignUpView(CreateView):
    model = User
    form_class = OperatorSignUpForm
    template_name = 'registration/signup_form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'operator'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # 前面一定要加/ 不然就不是从根url来的了
        # 重定向回控制台
        return redirect('/accounts/dashboard')


@login_required
@operator_required
def tables(request):
    return render(request, 'db0/data_tables.html')

@login_required
@operator_required
def statics(request):
    return render(request, 'db0/statistical_chart.html')

@login_required
@operator_required
def settings(request):
    return render(request, 'db0/device_setting.html')

@login_required
@operator_required
def valueInputSetting(request):
    return render(request, 'db0/value_limit_input.html')
    