# author:LWZ
# datetime:2021/2/21 16:08

"""
文件说明：

"""
from flask import Flask, session, redirect, render_template, url_for, flash
from flask_ckeditor import CKEditor
from dir06_forms import richtexteditor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
ckeditor = CKEditor(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    form = richtexteditor()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        flash('Your post is published!')
        return render_template('post.html', title=title, body=body)
    return render_template('ckeditor.html', form=form)
