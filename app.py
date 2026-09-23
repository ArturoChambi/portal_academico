from flask import Flask, render_template,request,session,redirect,url_for

app = Flask(__name__)

usuarios = {
"juan": "1234",
"maria": "abcd",
"pedro": "2026"
}

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login',methods=['GET','POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        
        if username in usuarios and usuarios[username] == password:
           
            session['usuario'] = username
            
            return redirect(url_for('cursos'))
        else:
            
            error = "Usuario o contraseña incorrectos."

    return render_template('login.html', error=error)
@app.route('/cursos')
def cursos():
    return render_template('cursos.html')
@app.route('/')
def logout():
    return f"Se cerro la sesion"


if __name__=='__main__':
    app.run(debug=True)

