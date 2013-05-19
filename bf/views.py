from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView

from bf.models import Race


class RaceList(ListView):
    """
    ApplicationList generates a list of all the objects specified in model.
    model = Race is equivalent to queryset = Race.objects.all()
    """
    model = Race
    template_name = 'bf/index.html'

