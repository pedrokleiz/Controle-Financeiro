from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('website.urls')),
    path('entrada/', include('website.urls')),
    path('saida/', include('website.urls')),
    path('extrato/', include('website.urls'))

]
