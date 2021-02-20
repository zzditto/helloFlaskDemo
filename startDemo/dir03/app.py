# author:LWZ
# datetime:2021/2/20 14:35

"""
文件说明：

"""
from flask import Flask, render_template, flash, redirect, url_for, session, send_from_directory
from formsDemo1 import LoginForm, UploadForm
import os
import uuid

app = Flask(__name__)

app.secret_key = "dev"
app.config['WTF_I18N_ENABLED'] = False
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024 # 3m
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')


@app.route("/", methods=['GET', 'POST'])
def index():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        flash(f"Welcome home, {username}")
        return redirect(url_for('index'))

    return render_template("index.html", form=form)


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = random_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('Upload success')
        session['filenames'] = [filename]
        return redirect(url_for('show_img'))
    return render_template('upload.html', form=form)


@app.route("/show_images", methods=['GET', 'POST'])
def show_img():
    return render_template('showImg.html')


@app.route("/upload/<path:filename>")
def get_fullPath(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)
