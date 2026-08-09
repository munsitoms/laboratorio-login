from flask import Flask, render_template_string, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///laboratorio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(80), unique=True, nullable=False)
    passwordHash = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/login', methods=['POST'])
def login():
    userNameInput = request.form.get('userName', '')
    passwordInput = request.form.get('password', '')

    user = User.query.filter_by(userName=userNameInput).first()

    if user and check_password_hash(user.passwordHash, passwordInput):
        return f'Bienvenido, {user.userName}. ¡Conectado a la Base de Datos!'
    
    return 'Credenciales incorrectas.'

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
        
        if not User.query.first():
            testUser = User(userName='admin', passwordHash=generate_password_hash('1234'))
            db.session.add(testUser)
            db.session.commit()
            
    app.run(debug=True)