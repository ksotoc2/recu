# Proyecto Django

Este es un proyecto desarrollado con Django. Aquí se describen los pasos para configurar y ejecutar el entorno local.

---

## 🔧 Requisitos

- Python 3.10 o superior
- Git

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/ksotoc2/recu.git
cd recu
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

- En **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- En **Linux / macOS**:

  ```bash
  source venv/bin/activate
  ```

### 4. Instalar dependencias del proyecto

```bash
pip install -r requirements.txt
```


---

## 🚀 Ejecutar el servidor de desarrollo

Después de activar el entorno virtual y haber instalado las dependencias, ejecuta:

```bash
python manage.py runserver
```

Luego abre tu navegador en:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛠 Migraciones y base de datos

En caso de que no tengas la base de datos creada, realiza lo siguiente:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Crear superusuario (opcional, para acceder al admin)

```bash
python manage.py createsuperuser
```

---

## 📌 Notas

- El entorno virtual está **excluido por `.gitignore`**.
- No olvides actualizar el archivo `requirements.txt` si instalas nuevas librerías.
- Usa el panel de administración de Django en [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) con tu superusuario.
