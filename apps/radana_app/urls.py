from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('items',views.items),
    path('items/<int:item_id>',views.item_detailes),
    path('checkout',views.checkout),
    # path('purchase/<int:item.id>',views.purchase_item),
    path('cart/<int:item_id>',views.add_to_cart),
    path('logout',views.logout)
]