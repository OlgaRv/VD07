from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Создаём приложение Flask
app = Flask(__name__)

# Настраиваем базу данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Создаем экземпляр (объект)базы данных
db = SQLAlchemy(app)

# Определяем модель (таблицу в базе данных)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User {self.username}, {self.email}>'

# Создаем таблицу в базе данных при первом запуске
with app.app_context():
    db.create_all()

# Добавляем запись в таблице
@app.route('/add_user')
def add_user():
    new_user = User(username='john', email='lTqQs@example.com')
    db.session.add(new_user)
    db.session.commit()
    return 'User added'

# Выводим содержимое таблицы в консоль для отладки (получаема записи из таблицы)
@app.route('/users')
def get_users():
    users = User.query.all()
    return str(users)

if __name__ == '__main__':
    app.run(debug=True)