import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import Rol

print("=== Roles en la BD ===")
for r in Rol.objects.all():
    print(r.id, r.nombre_rol)
