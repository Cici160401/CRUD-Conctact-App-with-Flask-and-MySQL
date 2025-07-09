from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL, cursors
from dotenv import load_dotenv
import os

#Cargar variables desde el archivo .env
load_dotenv()

app = Flask(__name__)
#Cargamos la KEY
app.secret_key = os.getenv('SECRET_KEY') 

#Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'coralito2025'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

################################### RUTA POR DEFECTO ############################################

@app.route('/')
def Index():
    #El html lo envía una ruta llamada Index, por eso llamaremos a los datos desde aqui
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    rows = cur.fetchall()
    #print(data) Para verificar si se listan

    #Convertir cada tupla en un diccionario usando sus nombres
    #para no tener que usar los índices de la tupla en el html,
    #sino llamar a los atributos por sus nombres.
    contacts= []
    for row in rows:
        contact ={
            'id' : row[0],
            'fullname' : row[1],
            'phone' : row[2],
            'email' : row[3],
        }
        contacts.append(contact)
    return render_template('index.html' , contacts = contacts)


################################### RUTA GET ############################################

@app.route('/get_contact', methods=['GET'])
def get_contact():
    if request.method  == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM contacts')
        data = cur.fetchall() #Lista de tuplas   
        return url_for(redirect('Index'))
 
################################### RUTA POST ############################################

@app.route('/add_contact', methods=['POST'])
def add_contact(): #método para añadir un contacto
    if request.method == 'POST':
        #guardamos nuestras request en variables
        fullname = request.form['fullname'].strip()
        phone = request.form['phone'].strip()
        email = request.form['email'].strip()
        #imprimimos en consola para asegurarnos
        print(f"fullname: '{fullname}'")
        print(f"phone: '{phone}'")
        print(f"email: '{email}'")
        #validación básica
        # Validación: campos vacíos
    if not fullname or not phone or not email:
        flash("All the fields are required to save.")
        return redirect(url_for('Index'))

    # Guardar en la base de datos
    cur = mysql.connection.cursor()
    cur.execute(
        'INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',
        (fullname, phone, email)
    )
    mysql.connection.commit()
    flash('Contacto añadido correctamente.')
    
    return redirect(url_for('Index'))
        
   

################################### RUTA EDIT ############################################

@app.route('/edit/<id>')
def edit_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id=%s',(id,))
    data = cur.fetchall() 
    print(data)
    
    return render_template('edit-contact.html', contact = data[0])

################################### RUTA UPDATE ############################################


@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
    cur=mysql.connection.cursor()
    cur.execute("""
        UPDATE contacts
        SET fullname=%s,
            phone=%s,
            email=%s
        WHERE id=%s        
    """, (fullname,phone, email, id))
    mysql.connection.commit()
    flash('Contact  updated succesfully')
    return redirect(url_for('Index'))

################################### RUTA DELETE ############################################

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    ######### VERSIÓN ANTERIOR DE COMO LLAMAR A LOS ATRIBUTOS USANDO
    ######### EL ÍNDICE DE LA TUPLA 
    #cur.execute('DELETE FROM contacts WHERE id= {0}'.format(id))
    cur.execute('DELETE FROM contacts WHERE id = %s', (id,))
    mysql.connection.commit()
    flash('Contact removed succesfully')
    return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(port = 3000, debug=True)