# Creando Usuario
```
adduser django
delsuer django
```

# entramos al usuario
```
su - django
```

usermod -aG sudo django

# Instalamos
```
sudo apt install python-virtualenv
```

# Creamos un enterno virtual
```
virtualenv .venv --python=python3
```

# Ver Carpetas ocultas
```
ls -la
```

# Activamos el enterno
```
source ~/.venv/bin/activate
```

# Instalar Django
```
pip install Django
pip install psycopg2
```

# Clonamos el repositorio
```
git clone https://marlonfalcon@bitbucket.org/marlonfalcon/erp.git
```

# instalo Ngix
```
sudo apt-get install nginx -y
cd /etc/nginx/sites-available
git clone https://github.com/falconsoft3d/ngix-para-odoo-erp/
cd ngix-para-odoo-erp/
sudo cp /etc/nginx/sites-available/ngix-para-odoo-erp/default.conf /etc/nginx/sites-available/default.conf
cd ..
mv default default-temp
mv default.conf default

cd /etc/nginx/sites-available
nano default
```

```
nginx -s reload
```

# Correr server de prueba
```
python manage.py runserver 0.0.0.0:8000
```

# nano settings.py
```
try:
    from local_settings import *
except ImportError:
    pass
```

# nano local_settings.py
```
ALLOWED_HOSTS = ['186.64.123.44']
```

# Intalamos gunicorn para levanntar sistemas webs por wwsgi
El Servidor Gunicorn El también conocido como Green Unicorn (Unicornio Verde). Este es un servidor HTTP para Python que soporta WSGI, Django y Paster de forma nativa; consume pocos recursos en ejecución y es bastante rápido. Gunicorn nos permite administrar las peticiones simultáneas que nuestra aplicación recibe y que cuenta con una serie de hooks que permite ejecutar código Python en los diferentes puntos de ejecución: on_start, when_ready on_reload, pre_fork post_fork (y otros) que lo hacen más extensible.

```
pip install gunicorn
```
# probamos que funcione
```
gunicorn --bind 0.0.0.0:8000 erp.wsgi
```

# Creamos el servicio
```
nano /etc/systemd/system/gunicorn.service
```
# Creamos el servicio
```
[Unit]
Description=Django ERP
After=network.target

[Service]
User=django
Group=www-data
WorkingDirectory=/home/django/erp
ExecStart=/home/django/.venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/django/erp/erp.sock erp.wsgi:application

[Install]
WantedBy=multi-user.target
```




