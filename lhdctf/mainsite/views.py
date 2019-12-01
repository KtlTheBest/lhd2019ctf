# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.core.exceptions import PermissionDenied

from django.views import generic
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper

from django.contrib.auth import login, authenticate, logout

from .forms import LoginForm

class IndexPage(generic.View):
    template_name = 'mainsite/index.html'

    def get(self, request):
        return render(request, self.template_name)

class EasyFlagView(generic.View):
    template_name = 'mainsite/easy.html'
    template_flag = 'mainsite/easy_flag.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_flag)

class LoginPage(generic.View):

    form = LoginForm
    template_name = 'mainsite/login.html'

    def get(self, request):
        form = self.form
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            redResponse = redirect('profile')
            redResponse.set_cookie('loggedIn', username)
            return redResponse
        else:
            return render(request, self.template_name, {'error': "Wrong Username/Password!", 'form': self.form})

class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        response = HttpResponseRedirect('index')
        response.delete_cookie('loggedIn')
        return redirect('index') # maybe some special redirect?

class ProfileView(generic.View):

    template_name = "mainsite/profile.html"
    template_oracle = "mainsite/profile_oracle.html"

    def get(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied()

        try:
            loggedIn = request.COOKIES['loggedIn']
            if loggedIn == 'KtlTheBest'.lower():
                return render(request, self.template_oracle)
            else:
                return render(request, self.template_name)
        except:
            return render(request, self.template_name)

class TreasureView(generic.View):

    treasure_path = 'mainsite/static/treasure.zip'

    def get(self, request):
        try:
            loggedIn = request.COOKIES['loggedIn']
            if loggedIn == "KtlTheBest".lower():
                wrapper = FileWrapper(file(self.treasure_path))
                response = HttpResponse(wrapper, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(self.treasure_path)
                response['Content-Length'] = os.path.getsize(self.treasure_path)
                return response
            else:
                raise Http404
        except:
            raise Http404

# Create your views here.


