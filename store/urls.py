from django.urls import path

from store import views

urlpatterns = [
    path('', views.home, name='store'),
    # path('cart/', views.CartListView.as_view(), name='cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    
]
