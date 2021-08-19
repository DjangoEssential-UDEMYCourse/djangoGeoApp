from django.shortcuts import render

from django.views.generic import View
from .utils import yelp_search, get_client_data

from django.utils.translation import gettext as _
from django.utils import translation


class IndexView(View):

    def get(self, request, *args, **kwargs):
        _lang_ = translation.get_language()  # seleciona o idioma atraves do navegador
        itens = []
        city = None

        while not city:
            ret = get_client_data()
            if ret:
                city = ret['city']

        resource = request.GET.get('key', None)
        loc = request.GET.get('loc', None)
        location = city

        context = {
            'city': city,
            'busca': False,
            'lang': _lang_,
        }

        if loc:
            location = loc
        if resource:
            itens = yelp_search(keyword=resource, location=location)
            context = {
                'itens': itens,
                'city': location,
                'busca': True,
                'lang': _lang_,
            }
        return render(request, 'index.html', context)
