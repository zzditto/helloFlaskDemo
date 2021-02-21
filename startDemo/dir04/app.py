# author:LWZ
# datetime:2021/2/21 13:49

"""
文件说明：

"""
from flask import Flask, url_for, redirect, render_template, session, flash
from form import upload_form, show_data
import os
import uuid
import pandas as pd

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dev'
app.config['TEMP_PATH'] = os.path.join(app.root_path, "temp")


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename


@app.route("/", methods=['GET', 'POST'])
def index():
    form = upload_form()
    if form.validate_on_submit():
        f = form.csvdata.data
        filename = random_filename(f.filename)
        f.save(os.path.join(app.config['TEMP_PATH'], filename))
        flash("upload success.")
        session['filenames'] = [filename]
        return redirect(url_for("showData", filename=filename))

    return render_template("upload.html", form=form)


@app.route("/showData/<path:filename>", methods=['GET'])
def showData(filename):
    file_path = os.path.join(app.config['TEMP_PATH'], filename)
    data = pd.read_csv(file_path).head()
    print(data)
    return render_template("showData.html", data=data)
