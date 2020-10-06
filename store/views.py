from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import *
# Create your views here.
class Store(View):

    def get(self, request, *args, **kwargs):

        products = Product.objects.all()
        context = {'products':products}
        return render(request, 'store/store.html', context)


class Cart(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total':0, 'get_cart_items':0}

        context = {'items':items, 'order':order}
        return render(request, 'store/cart.html', context)


class Checkout(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total':0, 'get_cart_items':0}

        context = {'items':items, 'order':order}

        return render(request, 'store/checkout.html', context)


class UpdateItem(View):

    def post(self, request, *args, **kwargs):
        # code to add order item

        return JsonResponse("Item was added", safe=False)
