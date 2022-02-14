from flask import Flask, render_template


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


app.run(host='localhost', port=8080, debug=True)
