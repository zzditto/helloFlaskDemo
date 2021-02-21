# author:LWZ
# datetime:2021/2/21 15:11

"""
文件说明：

"""
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileAllowed, FileRequired


class upload_file(FlaskForm):
    photo = FileField("Upload Image", validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField("Upload")
