# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from django.db.models import Q
from models import *
from forms import *
import an_api_wrapper
import re

@login_required(login_url='/login/')
def index(request):
	orderby = request.GET.get('orderby', '-date_created')
	query = request.GET.get('q', '')
	one_on_one_list = OneOnOne.objects.filter( Q(user_id=request.user.id) & Q(contact__last_name__icontains = query) | Q(contact__first_name__icontains = query) | Q(contact__email__icontains = query) ).order_by(orderby)
	page = request.GET.get('page', 1)
	paginator = Paginator(one_on_one_list, 20)
	try:
	    oneonones = paginator.page(page)
	except PageNotAnInteger:
	    oneonones = paginator.page(1)
	except EmptyPage:
	    oneonones = paginator.page(paginator.num_pages)

	return render(request, 'index.html', {'oneonones': oneonones, 'orderby':orderby, 'query':query})
	

def logout_user(request):
    logout(request)
    return redirect('/login/')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
		    form.save()
		    username = form.cleaned_data.get('username')
		    raw_password = form.cleaned_data.get('password1')
		    user = authenticate(username=username, password=raw_password)
		    login(request, user)
		    return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='/login/')
def create_one_on_one(request):
	if request.method == 'POST':
		contact_first_name = request.POST.get('first_name', '')
		contact_last_name = request.POST.get('last_name', '')
		contact_email = request.POST.get('email', '')
		oneonone_notes = request.POST.get('notes', '')
		errors = []

		#basic serverside validation
		if(contact_first_name == ''): errors.append('First Name is a required field')
		if(contact_last_name == ''): errors.append('Last Name is a required field')
		if(contact_email == ''): errors.append('Email is a required field')
		if(re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', contact_email) == None): errors.append('Valid email address is required')
		
		#if validation passes proccess the data in api and database
		if(errors == []):
			current_user = request.user
			#submit one on one data to action network using Tim's script
			an_response = an_api_wrapper.an_post(current_user.first_name, current_user.last_name, current_user.email, contact_first_name, contact_last_name, contact_email, oneonone_notes)
			
			if(an_response[0] == 200):
				#checking if contact exists, if so we use the id of the contact already in the system
				contact_search = Contact.objects.filter(email=contact_email);
				if(contact_search.count() != 0):
					new_contact = contact_search[0]
				else:	
					new_contact = Contact(first_name=contact_first_name, last_name=contact_last_name, email=contact_email)
					new_contact.save()

				#record one on one in db	
				new_oneonone = OneOnOne(user=current_user, contact = new_contact, description=oneonone_notes, form_endpoint = an_response[1], other_enpoint=an_response[2])
				new_oneonone.save()
				return redirect('/')

			errors.append('Error occured, unable to submit one on one form')

		contacts = Contact.objects.all()
		return render(request, 'oneonone/create.html', {'errors': errors, 'form_data': request.POST, 'contacts' : contacts })
	else:	
		contacts = Contact.objects.all()
		return render(request, 'oneonone/create.html', {'errors':[], 'form_data': {}, 'contacts' : contacts })

@login_required(login_url='/login/')
def edit_one_on_one(request, one_on_one_id):
	if request.method == 'POST':
		contact_first_name = request.POST.get('first_name', '')
		contact_last_name = request.POST.get('last_name', '')
		contact_email = request.POST.get('email', '')
		oneonone_notes = request.POST.get('notes', '')
		errors = []

		#basic serverside validation
		if(contact_first_name == ''): errors.append('First Name is a required field')
		if(contact_last_name == ''): errors.append('Last Name is a required field')
		if(contact_email == ''): errors.append('Email is a required field')
		if(re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', contact_email) == None): errors.append('Valid email address is required')
		
		#if validation passes proccess the data in api and database
		if(errors == []):
			current_user = request.user
			current_oneonone = OneOnOne.objects.get(pk=one_on_one_id)
			#submit one on one data to action network using Tim's script
			an_response = an_api_wrapper.an_put(current_oneonone.form_endpoint, current_oneonone.other_endpoint, current_user.first_name, current_user.last_name, current_user.email, contact_first_name, contact_last_name, contact_email, oneonone_notes)
			print an_response
			if(an_response[0] == 200):
				#checking if contact exists, if so we use the id of the contact already in the system
				current_contact = Contact.objects.get(pk=current_oneonone.contact_id)
				current_contact.first_name = contact_first_name
				current_contact.last_name = contact_last_name
				current_contact.email = contact_email
				current_contact.save()
				#record one on one in db	

				current_oneonone.description = oneonone_notes
				current_oneonone.save()
				return redirect('/')

			errors.append('Error occured, unable to submit one on one form')

		return render(request, 'oneonone/edit.html', {'errors': errors, 'form_data': request.POST, 'oneonone_id': one_on_one_id})
	else:
		oneonone_obj = OneOnOne.objects.get(pk=one_on_one_id)
		form_data = {
			'first_name': oneonone_obj.contact.first_name, 
			'last_name': oneonone_obj.contact.last_name, 
			'email': oneonone_obj.contact.email,
			'notes': oneonone_obj.description
		}
		return render(request, 'oneonone/edit.html', {'errors':[], 'form_data': form_data, 'oneonone_id': one_on_one_id})
