from django.urls import path, include
from .views import (index_view, deposit_view, withdrawal_view, statement_view)

urlpatterns = [
    path('index/', index_view),
    path('index/deposit/', deposit_view),
    path('index/withdrawal/', withdrawal_view),
    path('index/statement/', statement_view),


]
