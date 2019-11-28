# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext
from django.shortcuts import render

from django.views import generic

from .forms import LoginForm

class IndexPage(generic.View):
    template_name = 'mainsite/index.html'

    def get(self, request):
        return render(request, self.template_name)

class LoginView(generic.View):

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
            return redirect('mainsite:admin-page')
        else:
            return render(request, self.template_name, {'error': "Wrong Username/Password!", 'form': self.form})

class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('mainsite:index') # maybe some special redirect?

# Create your views here.


