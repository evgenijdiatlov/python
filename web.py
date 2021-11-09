# from logging import debug
# from flask import Flask, request, render_template


# app = Flask(__name__)


# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# #     print(request.method)
# #     return'''
# # <form action="/result" method="POST">
# #     <p>Name: <input type="text" name="name" /></p>
# #     <p>Math: <input type="text" name="math" /></p>
# #     <p>Send <input type="submit" name="Send!" /></p>
# # </form>
# #     '''

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     print(request.method)
#     return render_template('form.html')
# #можно извлечь файл с формой из папки либо прописать форму как выше внутри ретерна!!!
# # @app.route('/result', methods=['GET', 'POST'])
# # def result():
# #     print(request.form)
# #     return '''
# # <html>
# # <p>Страница пользователя</p>
# # <a href="/">Тык</a>
# # </html>    
# #     ''' 
# @app.route('/result', methods=['GET', 'POST'])
# def result():
#     print(request.method)
#     print(request.form)
#     return render_template('result.html', **request.form)
#     #return f'Result:{request.form.get("math")}'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)

import re
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.method)
    return render_template('form.html')


# @app.route('/result', methods=['GET', 'POST'])
# def result():
#     print(request.method)
#     print(request.form)
#     return render_template('result.html', result=request.form)

@app.route('/result', methods=['GET', 'POST'])
def result():
    if 'file' not in request.files:
        print('No file')
        return 'No file'
    file = request.file['file']
    print(file)
    return '200'

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



