# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from serializers import ResolutionSerializer
from permissions import OwnerPermission


def index(request):
    """
    homepage
    """

    return render_to_response("index.html",
                              RequestContext(request))



class ResolutionList(generics.ListCreateAPIView):
    """
    API endpoint that allows ithe authenticated user's resolutions to be viewed or edited.
    """

    serializer_class = ResolutionSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        """
        This view should return a list of all the resolutions
        for the currently authenticated user.
        """
        user = self.request.user
        return User.resolutions.all()
