# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from tourapp.models import Apartment, Owner

def index(request):
        apartments = Apartment.objects.all()
        return render_to_response("index.html",RequestContext(request,
                                             {
                                                 'apartments': apartments
                                                 }
                                             ))


