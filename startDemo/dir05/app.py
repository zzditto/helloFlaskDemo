# author:LWZ
# datetime:2021/2/21 14:47

"""
文件说明：

"""
from flask import Flask, url_for, session, redirect, render_template, flash, send_from_directory
import os
from forms import upload_file
from dir05_utils import serverUtils

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, "uploads")

serverUtil = serverUtils.serverUtils()


@app.route("/", methods=['GET', 'POST'])
def upload_img():
    form = upload_file()
    if form.validate_on_submit():
        f = form.photo.data
        filename = serverUtil.random_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash("Upload Success.")
        session['filenames'] = [filename]
        return redirect(url_for("showData"))

    return render_template("upload.html", form=form)


@app.route("/showData")
def showData():
    return render_template("showData.html")


@app.route("/showData/<path:filename>")
def get_full_path(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)
