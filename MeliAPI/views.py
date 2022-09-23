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
            used = search_form.cleaned_data['used_search']

            price_dict = {}

            official_response = apirequests.get('https://api.mercadolibre.com/sites/MLA/search?category='
                                                'MLA3025&official_store=all&q=' + urllib.parse.quote(search))
            if used:
                used_response = apirequests.get('https://api.mercadolibre.com/sites/MLA/search?category=MLA3025'
                                                '&condition=used&q=' + urllib.parse.quote(search))
                price_dict['used'] = data_organizer(used_response.json())

            price_dict['official_stores'] = data_organizer(official_response.json())

            context = {'message': search, 'results': price_dict, 'form': form, 'used': used}
            return render(request, 'MeliAPI/prices.html', context)

    else:
        context = {'message': 'Price search', 'form': form, 'hide': True}
        return render(request, 'MeliAPI/prices.html', context)


def data_organizer(response):
    data = []
    for element in response['results']:
        seller_name = urllib.parse.unquote(str(element['seller']['permalink'])).split('/')[3].replace('+', ' ')

        data.append({"title": element['title'], 'price': element['price'], 'seller': seller_name,
                     'image': element['thumbnail']})
    return data


def sales_manager(request):
    form_a = VentaForm
    form_b = CompraForm

    if request.POST:
        return render(request, 'MeliAPI/sales.html', {'form_a': form_a, 'form_b': form_b})

    else:
        return render(request, 'MeliAPI/sales.html', {'form_a': form_a, 'form_b': form_b})
