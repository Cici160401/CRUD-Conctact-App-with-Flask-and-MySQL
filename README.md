# CRUD de Contactos con Flask + QA Manual

Este es un proyecto de una aplicación web **CRUD** para gestionar contactos, desarrollada con **Flask** y conectada a una base de datos MySQL. Además, incluye un **proceso de pruebas manuales (QA Manual)** documentado para demostrar habilidades en testing funcional.

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Flask
- MySQL
- Jinja2
- HTML + Bootstrap (Bootswatch Theme)
- QA Manual (documentado abajo)

---

## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repo-crud-flask.git
   cd tu-repo-crud-flask
Crea y activa un entorno virtual:

bash
Copiar
Editar
python -m venv env
env\Scripts\activate  # En Windows
Instala los requisitos:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecuta la app:

bash
Copiar
Editar
python app.py
Abre en el navegador:

cpp
Copiar
Editar
http://127.0.0.1:3000
🧪 QA Manual - CRUD Flask App
1. Resumen general del proyecto
Esta app permite crear, leer, actualizar y eliminar contactos. Muestra una tabla dinámica con los contactos y botones para editar/eliminar. Utiliza Flask y Jinja2 para las vistas, y se conecta a una base de datos MySQL.

Este proyecto representa mi primer ejercicio completo de backend + pruebas manuales funcionales (QA Manual).

2. Ambiente de pruebas
Navegador: Brave v1.64.122

Sistema operativo: Windows 11

URL: http://127.0.0.1:3000

Resolución: 1366x768

3. Casos de prueba
ID	Caso de prueba	Paso(s) a seguir	Resultado esperado	Resultado real	Estado
1	Crear contacto	Ingresar nombre, teléfono y correo y presionar "Save"	El contacto se guarda y aparece en la tabla	✅ Correcto	✅ Aprobado
2	Agregar contacto con campos vacíos	Todos los campos vacíos	Aparece alerta de campos vacíos	✅ Muestra alerta	✅ Aprobado
3	Agregar email inválido	Email: juan@@.com	Rechaza el dato	Guarda el contacto	❌ Fallido
4	Editar contacto	Cambiar nombre	Actualiza contacto	✅ Correcto	✅ Aprobado
5	Eliminar contacto	Clic en "Delete"	Contacto desaparece	✅ Correcto	✅ Aprobado
6	Editar con campos vacíos	Borrar campos y presionar "Actualizar"	No permite guardar	Guarda contacto vacío	❌ Fallido
7	Números en el nombre	Ingresar “Juan123” como nombre	Muestra advertencia	Permite guardar	❌ Fallido

4. Errores encontrados / bugs
Error	Descripción	Prioridad	Solución propuesta
Email no validado	Se permite guardar emails inválidos	Alta	Validación en frontend y backend

5. Conclusión y recomendaciones
Las funcionalidades principales del CRUD funcionan correctamente. Sin embargo, se detectaron fallas en las validaciones de entrada. Se recomienda agregar validaciones tanto en el cliente (HTML/JS) como en el servidor (Python/Flask) para evitar que se guarden datos incompletos o incorrectos.

📸 Capturas (opcional)
Puedes incluir aquí algunas imágenes del formulario, la tabla, y los errores detectados.

✨ Autora
Karla, ingeniera TI interesada en QA, backend y automatización con Selenium (JS).