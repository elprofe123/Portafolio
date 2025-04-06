import os
from django.contrib.auth.models import User # type: ignore

# Obtiene las credenciales de las variables de entorno
username = os.getenv('ADMIN_USERNAME')
email = os.getenv('ADMIN_EMAIL')
password = os.getenv('ADMIN_PASSWORD')

# Solo crea el superusuario si no existe
if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username, email=email, password=password)
        print(f"Superusuario '{username}' creado exitosamente.")
    else:
        print("El superusuario ya existe.")
else:
    print("Faltan variables de entorno para crear el superusuario.")
