from django.urls import path

from store import views

urlpatterns = [
    path('', views.home, name='store'),
    path('kurtha/', views.kurtha, name='kurtha'),
    path('saree/', views.saree, name='saree'),
    path('tshirt/', views.tshirt, name='tshirt'),
    path('pant/', views.pant, name='pant'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process-order/', views.processOrder, name='process-order'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout')
    
]
