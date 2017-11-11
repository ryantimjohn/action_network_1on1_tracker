# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
# Create your views here.
def index(request):
	if request.user.is_authenticated():
		return render(request, 'index.html', {})
	return redirect('/login/')

def logout_user(request):
    logout(request)
    return redirect('/login/')