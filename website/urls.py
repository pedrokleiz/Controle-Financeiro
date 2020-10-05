from django.urls import path, include
from .views import pagina_entradas

urlpatterns = [
    path('', pagina_entradas),

]
