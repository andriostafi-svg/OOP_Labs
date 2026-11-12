# Лабораторна робота №9. Веб-додаток на Flask
from flask import Flask, render_template, request

app = Flask(__name__)
users = []   # список зареєстрованих користувачів


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = {'name': request.form['name'],
                'email': request.form['email'],
                'message': request.form['message']}
        users.append(user)
        return render_template('result.html', **user)
    return render_template('register.html')


@app.route('/users')
def users_list():
    return render_template('users.html', users=users)


@app.route('/news')
def news():
    items = ["Відкрито реєстрацію на курс Python",
             "Додано сторінку новин",
             "Сайт отримав нове оформлення"]
    return render_template('news.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
