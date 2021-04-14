from django.urls import path
from permisos.views import PermisosViews, PermisoDetailViews

app_name = "Permisos"
urlpatterns = [
    path('', PermisosViews.as_view()),
    path('<pk>/', PermisoDetailViews.as_view())
]

