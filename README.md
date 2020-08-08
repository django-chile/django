#Instalar Django

```
python3 -m pip install virtualenv
virtualenv venv -p python3
source venv/bin/activate
pip install django
django-admin startproject myproject
cd myproject
python manage.py runserver
http://127.0.0.1:8000/
```

Django Ayuda
# Creamos un entorno virtual "myvenv"
```
virtualenv myvenv
```

# Creamos un entorno virtual "env" con python3
```
virtualenv env --python=python3
cd env
source bin/activate
```

# desactivar entorno virtual "env"
```
deactivate
```

# Instalar django
```
pip install Django==1.9.1
```

# Instalar django 2
```
pip install Django
sudo apt-get install python3-psycopg2
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

# Migraciones
```
python manage.py migrate
python manage.py makemigrations
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
# Creando Apps 
```
python manage.py startapp moviesmfh
django-admin startapp mascota
```

# Saber librerias PIP
```
pip freeze
```
