from django.shortcuts import render
from django.views.generic import TemplateView


class InstantSearchView(TemplateView):
    template_name = "instant_search_view.html"
