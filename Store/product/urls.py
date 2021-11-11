from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/<slug:slug>/', views.detalles_producto, name='detalles_producto'),
]