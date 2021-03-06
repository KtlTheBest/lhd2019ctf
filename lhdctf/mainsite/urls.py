from django.conf.urls import url
from django.views.generic import TemplateView
from mainsite import views

urlpatterns = [
        url(r'^$', views.IndexPage.as_view(), name='index'),
        url(r'^robots\.txt$', TemplateView.as_view(template_name="mainsite/robots.txt", content_type='text/plain')),
        url(r'easy', views.EasyFlagView.as_view(), name='easy'),
        url(r'^login', views.LoginPage.as_view(), name='login'),
        url(r'^logout', views.LogoutView.as_view(), name='logout'),
        url(r'^profile', views.ProfileView.as_view(), name='profile'),
        url(r'^secret.zip$', views.TreasureView.as_view(), name='secret'),
        url(r'^confession.txt', TemplateView.as_view(template_name="mainsite/confession.txt", content_type='text/plain')),
        #url(r'login/$', views.loginPage, name='login')
]
