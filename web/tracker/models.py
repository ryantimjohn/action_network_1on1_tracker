# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

	
# Created a profile model
class Organizer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	action_network_id = models.CharField(max_length=36)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

class Contact(models.Model):
	organizer = models.ForeignKey(Organizer, blank=True, null=True)
	action_network_id = models.CharField(max_length=36, blank=True, null=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=62)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	
#Join Table
class OneOnOne(models.Model):
	organizer = models.ManyToManyField(Organizer)
	contact = models.ManyToManyField(Contact)
	description = models.TextField(blank=True, null=True)
	form_endpoint = models.URLField(max_length=2083)
	other_enpoint = models.URLField(max_length=2083)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)


