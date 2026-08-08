from flask import Flask, render_template_string, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

mockDatabase = {
    'admin': generate_password_hash('1234')
}

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/login', methods=['POST'])
def login():
    userName = request.form.get('userName', '')
    password = request.form.get('password', '')

    if userName in mockDatabase:
        if check_password_hash(mockDatabase[userName], password):
            return f'Bienvenido, {userName}. ¡Ingreso seguro exitoso!'
    
    return 'Credenciales incorrectas.'

if __name__ == '__main__':
    app.run(debug=True)