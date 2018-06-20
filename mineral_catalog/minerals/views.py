from django.shortcuts import get_object_or_404, render
from django.db.models import Max

import random

from .models import Mineral


def mineral_list(request):
    """Show the list of all minerals."""
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html',
                    {'minerals': minerals})


def mineral_detail(request, pk):
    """Show the detail of a mineral."""
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html',
                    {'mineral': mineral})


def random_mineral(request):
    """Show the detail of a random mineral."""
    max_id = Mineral.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_id)
    mineral = Mineral.objects.get(pk=pk)
    return render(request, 'minerals/mineral_detail.html',
                    {'mineral': mineral})
