from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

import datetime as DT
from django.shortcuts import render, get_object_or_404
import logging
from random import randint, choice, choices
from .models import Order, Item, Client



# Create your views here.
logger = logging.getLogger(__name__)

def index(request):
    logger.info(f'{request} index.html')
    context = {"title": "Shop"}
    return render(request, "app_03_shop/index.html", context)

def view_all_clients(request):
    context = {'clients': Client.objects.all(),
               'title': "Список клиентов",
               }
    return render(request, 'app_03_shop/template_clients_list.html', context)


def view_all_items_ordered_by_client(request, client_id, days):

    client = Client.objects.get(id=client_id)

    today = DT.date.today()
    previous = today - DT.timedelta(days=days)

    orders = []
    orders = Order.objects.order_by('order_date').filter(client_id=client, order_date__range=[previous, today])

    items = []
    tup = ()
    for order in orders:
        item_list = list(Order.objects.get(id=order.id).item_id.all())
        print(item_list)
        for item_1 in item_list:
            print(Order.objects.get(id=order.id).order_date)
            tup = (item_1, Order.objects.get(id=order.id).order_date)
            items.append(tup)
    print(items)

    context = {'client': client,
               'title': "Список заказов клиента",
                'items': items,
               }
    return render(request, 'app_03_shop/template_all_items_by_client.html', context)


def view_all_orders_by_client(request, client_id):

    client = Client.objects.get(id=client_id)

    orders = []
    orders = Order.objects.order_by('order_date').filter(client_id=client)
    print(orders)

    result = []
    tup = ()
    for order in orders:
        tup = (order, list(Order.objects.get(id=order.id).item_id.all()))
        result.append(tup)
    print(result)

    # items = Order.objects.order_by('order_date').filter(client_id=client).all().values_list()
    # items = Item.objects.filter(id=Order.objects.order_by('order_date').filter(client_id=client).first)

    context = {'client': client,
               'title': "Список заказов клиента",
               'result': result
               }
    return render(request, 'app_03_shop/template_all_orders_by_client.html', context)