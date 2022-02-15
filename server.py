from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин)', validators=[DataRequired()])
    password = PasswordField('Пароль)', validators=[DataRequired()])
    submit = SubmitField('Войти')


app = Flask('Sus')
app.config['SECRET_KEY'] = 'g987aef876a8ga89j70872hqiuhoi23lh5hu2p5yg1ui3gf1t34fi71t3f'


@app.route('/')
@app.route('/index/<title>')
def index(title='Home'):
    return render_template('base.html', title=title)


@app.route('/list_prof/<ul>')
def list_prof(ul):
    param = dict()
    param['title'] = 'Домашняя страница'
    param['prof_list'] = ['Мемодел', 'Амогус', 'Кот', 'Человек!', 'Убивец', 'Человек, написавший этот код)']
    if ul == 'ul':
        param['ul'] = 1
    elif ul == 'ol':
        param['ul'] = 0
    else:
        param['ul'] = 2
    return render_template('prof_list.html', **param)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {'title': 'Анкета', 'surname': 'Амогусов', 'name': 'Sus', 'education': 'выше всяческих похвал',
             'profession': 'Импостер', 'sex': 'Подвижный грунтовый ракетный комплекс 15П645 (РСД-10) «Пионер»',
             'motivation': 'секретно', 'ready': True}
    return render_template('answer.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/success')
def success():
    return render_template('success.html')


app.run(host='localhost', port=8080, debug=True)
