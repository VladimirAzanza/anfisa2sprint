from django.shortcuts import render

from .models import IceCream


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    ice_cream = IceCream.objects.get(pk=pk)
    context = {'ice_cream': ice_cream}
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    context = {}
    return render(request, template, context)
