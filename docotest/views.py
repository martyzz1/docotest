# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from serializers import ResolutionSerializer
from models.resolution import Resolution
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class IndexView(View):

    def get(self, request):
        """
        homepage
        """

        return render_to_response("index.html",
                              RequestContext(request))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class ResolutionMixin(object):

    serializer_class = ResolutionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the resolutions
        for the currently authenticated user.
        """
        user = self.request.user
        return Resolution.objects.all().filter(author=user)


class ResolutionList(ResolutionMixin, generics.ListCreateAPIView):
    """
    API endpoint that allows ithe authenticated user's resolutions to be viewed or edited.
    """

    #serializer_class = ResolutionSerializer
    #permission_classes = (IsAuthenticated,)

    #def get_queryset(self):
        #"""
        #This view should return a list of all the resolutions
        #for the currently authenticated user.
        #"""
        #user = self.request.user
        #return Resolution.objects.all().filter(author=user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ResolutionDetail(ResolutionMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update or delete a single resolution
    """

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
