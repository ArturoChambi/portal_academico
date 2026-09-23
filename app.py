from flask import Flask, render_template, request, redirect, url_for, session, make_response,flash

app = Flask(__name__)
app.secret_key = 'clave_secreta'


usuarios = {
    "juan":  "1234",
    "maria": "abcd",
    "pedro": "2026"
}


cursos = [
    {"nombre": "Programación Web", "docente": "Luis Pérez", "cupos": 15},
    {"nombre": "Bases de Datos", "docente": "Ana López", "cupos": 8},
    {"nombre": "Inteligencia Artificial", "docente": "Carlos Rojas", "cupos": 0}
]


@app.route('/')
def index():
    usuario_preferido = request.cookies.get('usuario_preferido')
    return render_template('index.html', usuario_preferido=usuario_preferido)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if username in usuarios and usuarios[username] == password:
           
            session['usuario'] = username
            respuesta = redirect(url_for('lista_cursos'))
            respuesta.set_cookie('usuario_preferido', username, max_age=60*60*24*30)
            return respuesta
        else:
            
            error = "Usuario o contraseña incorrectos."

    return render_template('login.html', error=error)


@app.route('/cursos')
def lista_cursos():
    
    return render_template('cursos.html', cursos=cursos)


@app.route('/perfil')
def perfil():
   
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('perfil.html', usuario=session['usuario'])


@app.route('/logout')
def logout():
    session.clear()
    flash("Sesion cerrada correctamente.")
    return redirect(url_for('index'))

@app.route('/eliminar_cookie')
def eliminar_cookie():
    respuesta = redirect(url_for('index'))
    respuesta.delete_cookie('usuario_preferido')
    return respuesta

if __name__ == '__main__':
    app.run(debug=True)
