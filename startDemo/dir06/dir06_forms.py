# author:LWZ
# datetime:2021/2/21 16:11

"""
文件说明：

"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_ckeditor import CKEditorField


class richtexteditor(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(1, 50)])
    body = CKEditorField("Body", validators=[DataRequired()])
    submit = SubmitField("Publish")
