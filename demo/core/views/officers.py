from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from ..forms import OfficerSignUpForm
from ..decorators import operator_required
from ..models import User

# 不能是def一个方法，需要定义一个类
class OfficerSignUpView(CreateView):
    model = User
    form_class = OfficerSignUpForm
    template_name = 'registration/signup_form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'officer'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/dashboard')
    