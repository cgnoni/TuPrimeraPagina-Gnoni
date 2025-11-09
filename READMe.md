# Proyecto Django: Blog de Recetas

## 📌 Descripción
Este proyecto es una pequeña web desarrollada en **Django** siguiendo el patrón **MVT (Model - View - Template)**.  
Permite crear, listar, visualizar y eliminar recetas de cocina. 

## 🧠 Funcionalidades
- Herencia de templates (base.html)
- Modelo único: Receta (con título, descripción e ingredientes)
- Formulario para agregar nuevas recetas.
- En formulario, boton para eliminar receta.
- Vista con listado de recetas guardadas.
- Boton para volver al inicio, si se lo requiere.
- Navbar de navegación en todas las páginas.

## ⚙️ Cómo ejecutar el proyecto
1. Ejecutar migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

2. Iniciar el servidor:
   ```bash
   python manage.py runserver

3. Abrir el navegador y visitar:
- 🏠 http://127.0.0.1:8000/ → Página de inicio

- 📜 /lista/ → Listado de recetas

- ➕ /nueva/ → Agregar una nueva receta

## 🧾 Requisitos

Los paquetes necesarios están listados en el archivo requirements.txt

## 📖 Orden para probar las funcionalidades

1. Ingresar al inicio (/)

2. Navegar a "Agregar Receta" para crear una nueva.

3. Volver al listado (/lista/) y verificar que se muestra.

4. Usar los botones de navegación (volver al inicio, navbar, eliminar receta)