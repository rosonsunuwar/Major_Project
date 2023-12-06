from django.urls import path

from store import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='store'),
    path('saree/', views.SareeListView.as_view(), name='saree'),
    path('kurtha/', views.KurthaListView.as_view(), name='kurtha'),
    path('t_shirt/', views.T_ShirtListView.as_view(), name='t_shirt'),
    path('pant/', views.PantListView.as_view(), name='pant'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
