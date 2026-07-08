from django.contrib import admin
from django.urls import path
from api.views import submit_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/orders/', submit_order),
]