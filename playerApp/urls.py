from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Usar una cadena vacía para que sea la URL de inicio.
    path("", views.index, name="index"),
    path('add_default/', views.add_default, name='add_default'),
    path('displayer/<int:item_id>/', views.displayer, name='displayer'),
    path('ok/', views.ok, name='ok'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)