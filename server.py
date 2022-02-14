from flask import Flask, render_template


app = Flask('Sus')


@app.route('/')
@app.route('/index/<title>')
def index(title='Home'):
    return render_template('base.html', title=title)


app.run(host='localhost', port=8080, debug=True)
