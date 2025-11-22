# Blog de Recetas – Camila Gnoni

Blog de recetas desarrollado en **Django 5.2**, con gestión de usuarios, CRUD de recetas, subida de imágenes, y diseño moderno con **Bootstrap 5**.

Este proyecto fue desarrollado como práctica avanzada de Python y Django, combinando funcionalidades de backend y frontend en un proyecto completo.

---

## 🛠 Tecnologías utilizadas

- Python 3.13  (requeriments.txt)
- Django 5.2.8  (requeriments.txt)
- Bootstrap 5.3  
- SQLite (base de datos por defecto)  
- HTML, CSS y JavaScript básicos

---

## ⚡ Funcionalidades

### Usuarios
- Registro de usuario con `username`, `email` y `password`.  
- Login y logout seguros.  
- Perfil de usuario con foto y bio editable.

### Recetas
- CRUD completo de recetas:
  - Crear, editar, eliminar y ver detalle.  
  - Cada receta tiene: `titulo`, `ingredientes`, `instrucciones` e **imagen opcional**.  
- Subida y manejo de imágenes de recetas.  
- Listado de recetas con **búsqueda por título**.  
- Mensajes informativos si no hay recetas o si la búsqueda no arroja resultados.  
- Listado responsive con tarjetas visuales y botones de acción.

### Main
- Templates y vistas generales guardados en una sola aplicación, para más orden y prolijidad.
- Página de **Acerca de mí / About** con descripción personal, imagen y enlaces a LinkedIn y GitHub.

---

## 🗂 Estructura del proyecto

```
TuPrimeraPagina-Gnoni/
├── main/
│   ├── templates/main/ (base.html, inicio.html, acerca_de_mi.html)
├── recetas/
│   ├── templates/recetas/ (lista_recetas.html, detalle_receta.html, editar_receta.html)
│   ├── forms.py (Formulario de búsqueda y creación/edición)
│   ├── views.py (CBVs para CRUD y listado)
│   ├── models.py (Receta)
├── usuarios/
│   ├── templates/usuarios/ (login.html, registro.html, perfil.html, perfil_editar.html)
│   ├── views.py (Vistas de usuario)
│   ├── forms.py (PerfilForm, registro, login)
│   ├── models.py (Perfil)
├── media/ (carpeta de imagenes mas pesadas, alojada en .gitignore)
├── static/main/ (CSS, imágenes, JS)
├── db.sqlite3 (base de datos alojada en .gitignore)
├── venv (carpeta del entorno virtual alojada en .gitignore)
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚡ Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/cgnoni/TuPrimeraPagina-Gnoni.git
cd TuPrimeraPagina-Gnoni
```

2. Crear y activar un entorno virtual:

```bash
python -m venv venv
# Windows + Git Bash
venv/Scripts/activate
# Linux / Mac
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Aplicar migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crear superusuario (opcional, admin ya esta utilizado):

```bash
python manage.py createsuperuser
```

6. Ejecutar el servidor:

```bash
python manage.py runserver
```

---

## 🖼 Uso de imágenes

- Imágenes de recetas: se guardan en la carpeta `media/` (no están en el repositorio).  
- Archivos estáticos (logos, iconos, CSS) se encuentran en `static/`.

---

## 📝 Admin

- Todos los modelos (`Receta`, `Perfil`) están registrados en el panel de **administración de Django**.  
- Desde el admin se pueden gestionar usuarios y recetas.

---

## 🌐 Navegación principal

- Inicio: `/`  
- Listado de recetas: `/recetas/lista/`  
- Crear receta: `/recetas/nueva/`  
- Perfil de usuario: `/usuarios/perfil/`  
- Editar perfil: `/usuarios/perfil/editar/`  
- Acerca de mí: `/acerca-de-mi/`

---

## 📌 Notas

- El proyecto está preparado para **desarrollo local**.  
- Para producción, configurar `MEDIA_ROOT`, `MEDIA_URL` y servidor estático adecuadamente.  
- Mantener `.gitignore` actualizado para no subir imágenes pesadas de recetas.
