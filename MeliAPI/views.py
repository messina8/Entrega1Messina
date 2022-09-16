import urllib.parse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from MeliAPI.forms import *
import requests as apirequests


def prices(request):
    form = PriceCheckForm
    if request.GET:
        search_form = form(request.GET)
        if search_form.is_valid():

            search = search_form.cleaned_data['product_name']

            official_stores_response = apirequests.get(
                'https://api.mercadolibre.com/sites/MLA/search?category=MLA3025&official_store'
                '=all&q=' + urllib.parse.quote(search))
            used_response = apirequests.get('https://api.mercadolibre.com/sites/MLA/search?category=MLA3025'
                                            '&condition'
                                            '=used&q=' + urllib.parse.quote(search))
            price_dict = {
                'used': [],
                'official_stores': []
            }
            official_stores_results = official_stores_response.json()
            for element in official_stores_results['results']:
                seller_name = urllib.parse.unquote(str(element['seller']['permalink'])).split('/')[3].replace('+', ' ')
                price_dict['official_stores'].append(
                    {"title": element['title'], 'price': element['price'], 'seller': seller_name,
                     'image': element['thumbnail']})
            used_results = used_response.json()
            for element in used_results['results']:
                price_dict['used'].append(
                    {'title': element['title'], 'price': element['price'], 'image': element['thumbnail']})

            context = {'message': search, 'results': price_dict, 'form': form, 'hide': True}
            return render(request, 'MeliAPI/prices.html', context)

    else:
        context = {'message': 'Price search', 'form': form, 'hide': True}
        return render(request, 'MeliAPI/prices.html', context)
