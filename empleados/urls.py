from django.urls import path
from empleados.views import EmpleadosViews, EmpleadoDetailView

app_name = "Empleados"
urlpatterns = [
    path('', EmpleadosViews.as_view()),
    path('<pk>/', EmpleadoDetailView.as_view())
]

