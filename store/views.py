from django.shortcuts import render

from store.models import Saree, Kurtha, T_Shirt, Pant
from django.views import generic


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'store/store.html'


class SareeListView(generic.ListView):
    template_name= 'store/saree.html'
    models = Kurtha
    context_object_name = 'sarees'
    
    def get_queryset(self):
        return Saree.objects.all().order_by('name')
    
class KurthaListView(generic.ListView):
    template_name= 'store/kurtha.html'
    models = Kurtha
    context_object_name = 'kurthas'
    
    def get_queryset(self):
        return Kurtha.objects.all().order_by('name')
class T_ShirtListView(generic.ListView):
    template_name= 'store/t_shirt.html'
    models = T_Shirt
    context_object_name = 't_shirts'
    
    def get_queryset(self):
        return T_Shirt.objects.all().order_by('name')
    
class PantListView(generic.ListView):
    template_name= 'store/pant.html'
    models = Pant
    context_object_name = 'pants'
    
    def get_queryset(self):
        return Pant.objects.all().order_by('name')
    
def cart(request):
    return render (request, 'store/cart.html')
def checkout(request):
    return render (request, 'store/checkout.html')
