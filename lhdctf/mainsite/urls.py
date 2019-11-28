from django.conf.urls import url
from mainsite import views

urlpatterns = [
        url(r'^$', views.IndexPage.as_view(), name='index'),
        #url(r'login/$', views.loginPage, name='login')
]
