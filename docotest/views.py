# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from serializers import ResolutionSerializer
from models.resolution import Resolution


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
        return Resolution.objects.all().filter(author=user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
