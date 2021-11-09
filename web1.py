import os
import time
from flask import Flask, flash, request, redirect, url_for
from flask.templating import render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:\\Users\\HP\\Desktop\\python44'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def secure_filename(filename):
    cur_time = time.time()
    name, ext = filename.split('.')
    hash_name = hash(cur_time)
    new_filename = f'{name}_{hash_name}.{ext}'
    return new_filename


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        # import pdb; pdb.set_trace()
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return render_template('form.html')

from flask import send_from_directory

@app.route('/uploads/<name>')
def download_file(name):
    f = open(name, 'r')
    context = f.readlines()
    headers = context[0].split(';')
    body = context[1:]
    body = [x.split(';') for x in body]
    print(context)
    f.close()
    return render_template('table.html', headers=headers, body=body)
    # return send_from_directory(app.config["UPLOAD_FOLDER"], name)

if __name__ == '__main__':
    app.run(debug=True)