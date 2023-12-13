from django.urls import path

from store import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='store'),
    # path('cart/', views.CartListView.as_view(), name='cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
