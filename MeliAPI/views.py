
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
            response = apirequests.get('https://api.mercadolibre.com/sites/MLA/search?category=MLA3025&official_store'
                                       '=all&q=' + string_to_url(search))
            price_dict = {}
            results = response.json()
            for element in results['results']:
                name = apirequests.get('https://api.mercadolibre.com/users/' + str(element['seller']['id']))
                name = name.json()['nickname']
                price_dict[name] = element['price']

            context = {'message': search, 'results': price_dict, 'form': form, 'hide': True}
            return render(request, 'MeliAPI/prices.html', context)

    else:
        context = {'message': 'Price search', 'form': form, 'hide': True}
        return render(request, 'MeliAPI/prices.html', context)


def string_to_url(string):
    converted_string = ''
    for a in string:
        if a == ' ':
            a = '%20'
            converted_string += a
        else:
            converted_string += a

    return converted_string
