# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from rest_framework import filters
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

def detail(request, apt_id):
    try:
        Apt = Apartment.objects.get(pk=apt_id)
    except Apartment.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'apt': Apt})


class AptViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows groups to be viewed or edited.
    """
    queryset = Apartment.objects.all()
    serializer_class = AptSerializer

    def get_queryset( self):
        queryset = super(AptViewSet, self).get_queryset()
        cats_name = self.request.query_params.get('cats__name', None)
        if cats_name is not None:
            queryset = queryset.filter(cats__name=cats_name)
        return queryset