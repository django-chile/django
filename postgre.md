
# Instalando

```
pip install psycopg2
```

# Configuramos el gestor de BD settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'odoo',
        'PASSWORD': False,
        'HOTS': 'localhost',
        'PORT': 5432,
    }
}
```
