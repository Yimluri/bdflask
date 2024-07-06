from flask import Flask,request,render_template,flash,url_for,redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'
app.config['MYSQL_PORT'] = 3307

mysql = MySQL(app)
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
     try:
        cursor= mysql.connection.cursor()
        cursor.execute('select * from albums')
        consultaA= cursor.fetchall()
        print(consultaA)
        return render_template('index.html', albums=consultaA)
     except Exception as e:
         print(e)

@app.route('/editar/<id>')
def editar(id):
     cur= mysql.connection.cursor()
     cur.execute('select * from albums where idalbums=%s',[id])
     albumE= cur.fetchone()
     return render_template ('edit.html', albums = albumE)

@app.route('/editar2/<id>',methods=['POST'])
def editar2(id):
     if request.method== 'POST':
         Ftitulo=request.form['txtTitulo']
         Fartista=request.form['txtArtista']
         Fanio=request.form['txtAnio']
         
         cur2 = mysql.connection.cursor()
         cur2.execute('update albums set titulo= %s, artista= %s, anio= %s where idalbums= %s', (Ftitulo,Fartista,Fanio,id))
         mysql.connection.commit()

         flash('Registro guardado correctamente')
         return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
         
         cur2 = mysql.connection.cursor()
         cur2.execute('Delete from albums where idalbums= %s',[id])
         mysql.connection.commit()
         flash('Registro borrado correctamente')
         return redirect(url_for('index'))
              
         

@app.route('/guardarAlbum',methods=['POST'])
def guardarAlbum():

    if request.method== 'POST':
         Ftitulo=request.form['txtTitulo']
         Fartista=request.form['txtArtista']
         Fanio=request.form['txtAnio']
         
         cursor = mysql.connection.cursor()
         cursor.execute('insert into albums(titulo,artista,anio) values(%s,%s,%s)', (Ftitulo,Fartista,Fanio))
         mysql.connection.commit()
         flash('Registro guardado correctamente')
         return redirect(url_for('index'))
    
if __name__ == '__main__':
       app.run(port=3000,debug=True)
