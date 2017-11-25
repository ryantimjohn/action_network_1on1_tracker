# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=62, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	
#Join Table
class OneOnOne(models.Model):
	user = models.ForeignKey(User, to_field='id', null=True)
	contact = models.ForeignKey(Contact, to_field='id', null=True)
	description = models.TextField(blank=True, null=True)
	form_endpoint = models.URLField(max_length=2083)
	other_enpoint = models.URLField(max_length=2083)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)


