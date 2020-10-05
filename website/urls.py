from django.urls import path, include
from .views import index_view
from .views import deposit_view
from .views import withdrawal_view
from .views import statement_view

urlpatterns = [
    path('index/', index_view),
    path('deposit/', deposit_view),
    path('withdrawal/', withdrawal_view),
    path('statement/', statement_view),


]
