from django.contrib import admin
from django.urls import path

from api.views import apiOverview

urlpatterns = [
    path("", apiOverview)
]