from django.shortcuts import render

from django.views.generic import View
from .utils import yelp_search, get_client_data


class IndexView(View):

    def get(self, request, *args, **kwargs):
        itens = []
        city = None
        location = city

        while not city:
            ret = get_client_data()
            city = ret['city']

        resource = request.GET.get('key', None)
        loc = request.GET.get('loc', None)

        context = {
            'city': city,
            'busca': False,
        }

        if loc:
            location = loc
        if resource:
            itens = yelp_search(keyword=resource, location=location)
            context = {
                'itens': itens,
                'city': location,
                'busca': True
            }
        return render(request, 'index.html', context)
