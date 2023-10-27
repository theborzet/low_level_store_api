from django.urls import path

from products.views import ProductListView, NewGoodView

app_name = 'products'
urlpatterns = [
    path('list/', ProductListView.as_view(), name='list'),
    path('new_good/', NewGoodView.as_view(), name='add'),

]