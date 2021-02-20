# author:LWZ
# datetime:2021/2/20 14:35

"""
文件说明：

"""
from flask import Flask, render_template, flash, redirect, url_for
from formsDemo1 import LoginForm

app = Flask(__name__)

app.secret_key = "dev"
app.config['WTF_I18N_ENABLED'] = False


@app.route("/", methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        flash(f"Welcome home, {username}")
        return redirect(url_for('index'))

    return render_template("index.html", form=form)
