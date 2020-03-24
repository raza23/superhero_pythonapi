# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Hero
from .serializers import HeroSerializer


class HeroView(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

# Create your views here.
