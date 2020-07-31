from django.urls import include, path

from demo.core.views import dashboard, officers, operators


urlpatterns = [
    path('', dashboard.home, name='home'),
    # path('loged',name='data_tables')
]