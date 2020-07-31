"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from demo.core.views import dashboard, officers, operators

urlpatterns = [
    # 因为后续django-restful-framework的关系，app在project子目录下，需要注意app模块引用路径
    path('', include('demo.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # ''引号里的部分用在html模版里，交互使用！
    path('accounts/signup/', dashboard.SignUpView.as_view(), name='signup'),
    path('accounts/signup/operator', operators.DftStaffSignUpView.as_view(), name='operator_signup'),
    path('accounts/signup/operator/', officers.OfficerSignUpView.as_view(), name='officer_signup'),
    # 登陆进入系统超级管理员界面
    path('accounts/signup/admin/', admin.site.urls),
    # 重定向至dashboard界面，TODO：需要加登陆decorator
    path('accounts/dashboard/', dashboard.dashboard, name='dashboard'),
    # TODO:从dashboard跳转至其他页面需要重定向至应用core的urls设置规则
    path('accounts/signed_in/tables', dashboard.tables ,name='data_tables'),
    path('accounts/signed_in/statics', dashboard.statics ,name='statistical_chart'),
    path('accounts/signed_in/settings', dashboard.settings, name="device_setting"),
    path('accounts/signed_in/valueSetting', dashboard.valueInputSetting, name="value_limit_input"),
    path('accounts/signed_in/upload', dashboard.upload, name="upload_status"),
    
]




