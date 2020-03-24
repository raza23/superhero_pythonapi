# from django.contrib import admin
from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('superheros', views.HeroView)

urlpatterns = [
    url('', include(router.urls)),

]
