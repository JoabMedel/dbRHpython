from django.urls import path
from puestos.views import PuestosViews, PuestoDetailView

app_name = "Puestos"
urlpatterns = [
    path('', PuestosViews.as_view()),
    path('<pk>/', PuestoDetailView.as_view())
]
