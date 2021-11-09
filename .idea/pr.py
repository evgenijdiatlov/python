from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '''
<html>
<p>Выходи за меня, замуж!?</p>
<a href="/user/">Согласна</a>
</html>
    '''

@app.route('/user/')
def user():
    return '''
<html>
<p> Надька! знаешь что?</p>
<a href="/user/">Нажми</a>
</html>
    '''
