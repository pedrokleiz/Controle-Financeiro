from django.urls import path, include
from .views import (index_view, deposit_view, withdrawal_view,
                    statement_view, deposit_value_view, withdrawal_value_view)

urlpatterns = [
    path('index/', index_view, name='index'),
    path('index/deposit/', deposit_view, name='deposit'),
    path('index/deposit/depositvalue', deposit_value_view, name='depositValue'),
    path('index/withdrawal/withdrawalvalue',
         withdrawal_value_view, name='withdrawalValue'),
    path('index/withdrawal/', withdrawal_view, name='withdrawal'),
    path('index/statement/', statement_view, name='statement'),

]
