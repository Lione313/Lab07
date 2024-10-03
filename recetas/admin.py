from django.contrib import admin

from .models import Autor , Receta , Comentario , Evento ,Usuario, RegistroEvento


admin.site.register(Autor)
admin.site.register(Receta)
admin.site.register(Comentario)
admin.site.register(Evento)
admin.site.register(Usuario)
admin.site.register(RegistroEvento)