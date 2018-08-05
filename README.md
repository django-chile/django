# django
Django Ayuda
# Creamos un entorno virtual "myvenv"
```
virtualenv myvenv
```

# Creamos un entorno virtual "env" con python3
```
virtualenv env --python=python3
```

# Instalar django
```
pip install Django==1.9.1
```

# Crear una aplicación
```
django-admin startproject mysite
python manage.py startapp polls
```

# Correr la aplicacion
```
cd mysite
python manage.py runserver
```
# Ver la app
```
http://127.0.0.1:8000/
```

# Admin
```
http://127.0.0.1:8000/admin
```

# Creando Super Usuario
```
python manage.py createsuperuser
```
