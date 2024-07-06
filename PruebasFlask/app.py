from flask import Flask,request,render_template,flash,url_for,redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'clinicamedica'
app.config['MYSQL_PORT'] = 3307

mysql = MySQL(app)
app.secret_key = 'mysecretkey'


@app.route('/registroM')
def registro():
    return render_template('registro.html')

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/consultasM')
def consultas():
     try:
        cursor= mysql.connection.cursor()
        cursor.execute('select * from tbmedicos')
        consulta= cursor.fetchall()
        print(consulta)
        return render_template('consultasM.html', tbmedicos=consulta)
     except Exception as e:
         print(e)


@app.route('/guardarMedico',methods=['POST'])
def guardarAlbum():

    if request.method== 'POST':
         Krfc=request.form['txtRFC']
         Knombre=request.form['txtNombre']
         Kcedula=request.form['txtCedula']
         Kcorreo=request.form['txtCorreo']
         Kpassword=request.form['txtPassword']
         Krol=request.form['txtRol']
         
         cursor = mysql.connection.cursor()
         cursor.execute('insert into tbmedicos(rfc,nombre,cedula,correo,password,rol) values(%s,%s,%s,%s,%s,%s)', (Krfc,Knombre,Kcedula,Kcorreo,Kpassword,Krol))
         mysql.connection.commit()
         flash('Registro guardado correctamente')
         return redirect(url_for('consultas'))
if __name__ == '__main__':
       app.run(port=3000,debug=True)