from django.shortcuts import render

from store.models import *
from django.views import generic


# Create your views here.
class HomeView(generic.ListView):
    models= Product
    context_object_name = 'products'
    template_name = 'store/store.html'

    def get_queryset(self):
        return Product.objects.all()
    
    
# class CartListView(generic.ListView):
#     context_object_name = 'items'
#     template_name = 'store/cart.html'
#     def cart(request):
#         if request.user.is_authenticated:
#             customer = request.user.customer
#             order, created = Order.objects.get_or_create(customer= customer, complete= False)
#             items = order.orderitem_set.all()
#         else:
#             items = []
#     def get_queryset(self):
#         return OrderItem.objects.all()
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete= False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        
    context = {
        'items': items,
        'order': order,
    }
    return render (request, 'store/cart.html', context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete= False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        
    context = {
        'items': items,
        'order': order,
    }
    return render (request, 'store/checkout.html', context)
