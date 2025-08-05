# CRUD de Contactos con Flask + QA Manual

Aplicación web **CRUD** desarrollada con **Flask** y **MySQL**, que permite gestionar contactos. Incluye además un **proceso de QA Manual** para verificar funcionalidad y calidad.

---

## 🛠️ Tecnologías utilizadas

- **Backend**  
  - Python 3  
  - Flask  
  - MySQL  
- **Frontend**  
  - Jinja2  
  - HTML  
  - Bootstrap (Bootswatch Theme)  
- **Pruebas**  
  - QA Manual (ver sección)

---

## 🚀 Instalación y ejecución

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/tu-usuario/tu-repo-crud-flask.git
   cd tu-repo-crud-flask

---

## Crear y activar entorno virtual

python -m venv env

# En Windows
env\Scripts\activate

# En macOS/Linux
source env/bin/activate

## Instalar dependencias

pip install -r requirements.txt

## Ejecutar la aplicación
python app.py

## Abrir en el navegador
http://127.0.0.1:3000

## 🧪 QA Manual
1. Resumen del proyecto
Aplicación CRUD que permite Crear, Recuperar, Update y Delete contactos.

Se muestra una tabla dinámica con los contactos.

Botones para editar y eliminar.

Vistas con Flask y Jinja2.

Base de datos MySQL.

2. Ambiente de pruebas
Navegador: Brave v1.64.122

SO: Windows 11

URL: http://127.0.0.1:3000

Resolución: 1366 × 768

## Casos de prueba

```bash
ID  Caso de prueba                     Pasos a seguir                                                      Resultado esperado                              Resultado real          Estado
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1   Crear contacto                     Ingresar nombre, teléfono y correo; presionar Save                  El contacto se guarda y aparece en la tabla      Correcto               Aprobado
2   Agregar contacto con campos vacíos Dejar todos los campos vacíos; presionar Save                       Aparece alerta de campos vacíos                  Muestra alerta         Aprobado
3   Agregar email inválido             Email: juan@@.com; presionar Save                                   Rechaza el dato                                  Guarda el contacto     Fallido
4   Editar contacto                    Seleccionar un contacto; cambiar nombre; presionar Update           Actualiza datos del contacto                     Correcto               Aprobado
5   Eliminar contacto                  Clic en Delete                                                      El contacto desaparece de la tabla               Correcto               Aprobado
6   Editar con campos vacíos           Borrar campos; presionar Update                                     No permite guardar                               Guarda contacto vacío  Fallido
7   Números en el nombre               Nombre: Juan123; presionar Save                                     Muestra advertencia                              Permite guardar        Fallido


---


