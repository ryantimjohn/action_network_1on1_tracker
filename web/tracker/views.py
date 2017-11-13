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

def create_one_on_one(request):
	if request.method == 'POST':
		#use validator: https://github.com/pyeve/cerberus
		return HttpResponse("Create the item")
	else:	
		return render(request, 'oneonone/create.html', {})