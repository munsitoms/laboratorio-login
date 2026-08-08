from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/login', methods=['POST'])
def login():
    userName = request.form.get('userName', '')
    password = request.form.get('password', '')

    if userName == 'admin' and password == '1234':
        return f'Bienvenido, {userName}.'

    return 'Credenciales incorrectas.'

if __name__ == '__main__':
    app.run(debug=True)
