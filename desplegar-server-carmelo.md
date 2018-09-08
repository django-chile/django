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







