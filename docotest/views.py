# -*- coding: utf-8 -*-
from django.shortcuts import render
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

        user = request.user
        resolutions = user.resolutions.all()

        context = {
                    'resolutions': resolutions
                }

        return render(request, "index.html", context)

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
        print "getting queryset"
        user = self.request.user
        return Resolution.objects.all().filter(author=user)

    def perform_create(self, serializer):
        print "perform create using author1"
        print self.request.user
        serializer.save(author=self.request.user)


class ResolutionDetail(ResolutionMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update or delete a single resolution
    """

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def perform_create(self, serializer):
        print "perform create using author2"
        print self.request.user
        serializer.save(author=self.request.user)
