from django.urls import path, include
from .views import (index_view, deposit_view, withdrawal_view,
                    statement_view, deposit_value_view, withdrawal_value_view,
                    elements_view, deposit_success_view, withdrawal_success_view,
                    statement_result_view, deposit_result_view, withdrawal_result_view)

urlpatterns = [
    path('', index_view, name='index'),
    path('deposit', deposit_view, name='deposit'),
    path('deposit/result', deposit_result_view, name='depositResult'),
    path('deposit/depositvalue', deposit_value_view, name='depositValue'),
    path('withdrawal', withdrawal_view, name='withdrawal'),
    path('withdrawal/result', withdrawal_result_view, name='withdrawalResult'),
    path('withdrawal/withdrawalvalue',
         withdrawal_value_view, name='withdrawalValue'),
    path('elements', elements_view),
    path('deposit/depositvalue/depositsuccess',
         deposit_success_view, name='depositSuccess'),
    path('withdrawal/withdrawalvalue/withdrawalsuccess',
         withdrawal_success_view, name='withdrawalSuccess'),
    path('statement', statement_view, name='statement'),
    path('statement/result', statement_result_view, name='statementResult')
]
