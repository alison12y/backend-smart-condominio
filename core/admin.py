from django.contrib import admin
from .models import Usuario, Rol, Reservas, Pagos

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Reservas)
admin.site.register(Pagos)
