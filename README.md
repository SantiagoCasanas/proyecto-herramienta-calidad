# Proyecto congreso
Para ejecutar por primera vez
1. Clonar el proyecto en el escritorio usando una terminal de gitbash (clic derecho -> abrir gitbash) con uno de los siguientes comandos
- git clone https://github.com/SantiagoCasanas/proyecto-herramienta-calidad.git
- git clone git@github.com:SantiagoCasanas/proyecto-herramienta-calidad.git
3. Abrir una terminal de gitbash sobre la carpeta generada (clic derecho -> abrir gitbash)
4. Creamos un ambiente virtual: python -m venv venv
5. Activamos el ambiente: source venv/Scripts/activate
6. Instalamos Django: pip install django
7. Creamos las migraciones: python manage.py makemigrations asistente_diagnostico
8. Migramos la base de datos: python manage.py migrate
9. Creamos un superusuario: python manage.py createsuperuser (llenamos los datos que nos pide)
10. Corremos el proyecto: python manage.py runserver

Si deseas correr de nuevo el proyecto, otro día después de descargado:
1. Abrir gitbash en la carpeta del proyecto  (clic derecho -> abrir gitbash)
2. Activamos el ambiente: source venv/Scripts/activate
3. Corremos el proyecto: python manage.py runserver


Para cargar archivos en la GitHub

git add .
git commit -m "nuevos cambios 18"
git push origin main
