
from django.contrib import admin
from django.urls import path, include  
from recetas.views import crear_evento, registrar_usuario, listar_eventos 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_evento/', crear_evento, name='crear_evento'),  
    path('registrar_usuario/', registrar_usuario, name='registrar_usuario'),
    path('eventos/', listar_eventos, name='eventos'),
]
