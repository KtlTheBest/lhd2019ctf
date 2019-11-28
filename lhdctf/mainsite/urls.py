from django.conf.urls import url
from django.views.generic import TemplateView
from mainsite import views

urlpatterns = [
        url(r'^$', views.IndexPage.as_view(), name='index'),
        url(r'^robots\.txt$', TemplateView.as_view(template_name="mainsite/robots.txt", content_type='text/plain')),
        #url(r'login/$', views.loginPage, name='login')
]
