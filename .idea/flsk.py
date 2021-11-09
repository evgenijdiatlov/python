from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '''
<html>
<p>Выйдушь за меня замуж, моя любимая Надька</p>
<a href="/user/">Тык</a>
</html>
    '''

@app.route('/user/')
def user():
    return '''
<html>
<p>Знаешь, что Надька</p>
<a href="/">Нажми</a>
</html>