from django.urls import path, include
from .views import (index_view, deposit_view, withdrawal_view,
                    statement_view, deposit_value_view, withdrawal_value_view, elements_view, deposit_success_view, withdrawal_success_view)

urlpatterns = [
    path('', index_view, name='index'),
    path('deposit/', deposit_view, name='deposit'),
    path('deposit/depositvalue', deposit_value_view, name='depositValue'),
    path('withdrawal/', withdrawal_view, name='withdrawal'),
    path('withdrawal/withdrawalvalue',
         withdrawal_value_view, name='withdrawalValue'),
    path('statement/', statement_view, name='statement'),
    path('elements', elements_view),
    path('deposit/depositvalue/depositsuccess.html',
         deposit_success_view, name='depositSuccess'),
    path('withdrawal/withdrawalvalue/withdrawalsuccess',
         withdrawal_success_view, name='withdrawalSuccess')

]
