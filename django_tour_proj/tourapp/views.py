# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from rest_framework import viewsets

from tourapp.models import Apartment, Owner
from tourapp.serializers import AptSerializer


def index(request):
        apartments = Apartment.objects.all()
        return render_to_response("index.html",RequestContext(request,
                                             {
                                                 'apartments': apartments
                                                 }
                                             ))

class AptViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows groups to be viewed or edited.
    """
    queryset = Apartment.objects.all()
    serializer_class = AptSerializer
