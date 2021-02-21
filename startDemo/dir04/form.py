# author:LWZ
# datetime:2021/2/21 13:55

"""
文件说明：

"""
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, FileField
from flask_wtf.file import FileRequired, FileAllowed


class upload_form(FlaskForm):
    csvdata = FileField("Upload File", validators=[FileRequired(), FileAllowed(['csv'])])
    submit = SubmitField("upload")


class show_data(FlaskForm):
    showdata = TextAreaField("Show Data")
