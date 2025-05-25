Viandas Saludables

Viandas Saludables es una aplicación web desarrollada con Django para gestionar pedidos, productos y clientes de una tienda de viandas saludables. Este proyecto fue desarrollado para el curso de CoderHouse de Python. 

Autor: Manuel Alejandro Talavera Talavera

---

Tecnologias utilizadas

- Python 3.12+
- Django 5.2.1
- HTML5 + Django Templates
- SQLite3

---

Estructura del proyecto

viandas_saludables/
├── core/
│ ├── models.py
│ ├── forms.py
│ ├── views.py
│ ├── urls.py
│ └── templates/core/
│ ├── base.html
│ ├── home.html
│ ├── producto_form.html
│ ├── cliente_form.html
│ ├── pedido_form.html
│ ├── buscar.html
│ └── buscar_pedido.html
├── viandas_saludables/
│ ├── settings.py
│ ├── urls.py
├── manage.py
└── db.sqlite3


---

¿Cómo ejecutar el proyecto?

1. Clonar este repositorio:

    git clone https://github.com/TU_USUARIO/TuPrimeraPaginaTuApellido.git
    cd TuPrimeraPaginaTuApellido

2. Crear un entorno virtual y activarlo:

    python -m venv venv
    venv\Scripts\activate

3. Instalar Django

    pip install django

4. Aplicar migraciones

    python manage.py makemigrations
    python manage.py migrate

5. Crear Superuser

    python manage.py createsuperuser

6. Ejecutar Servidor

    python manage.py runserver

Funcionalidades disponibles

    Agregar producto → /producto/agregar/
    Agregar cliente → /cliente/agregar/
    Agregar pedido → /pedido/agregar/
    Buscar producto → /buscar/
    Buscar pedido → /buscar-pedido/
    Página de inicio → /
