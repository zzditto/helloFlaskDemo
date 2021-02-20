# author:LWZ
# datetime:2021/2/20 14:27

"""
文件说明：

"""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError


# 自定义验证器
def is_42(message=None):
    if message is None:
        message = "Must be 42."

    def _is_42(form, field):
        if field.data != 42:
            raise ValidationError(message)

    return _is_42


class MyBaseForm(FlaskForm):
    class Meta:
        locales = ['zh']


class LoginForm(MyBaseForm):
    username = StringField("Username", validators=[DataRequired(message="名称不能为空")], render_kw={'placeholder': 'Your username'})
    password = PasswordField("Passwrod", validators=[DataRequired(), Length(8, 128)])
    age = IntegerField("Age", validators=[is_42()])
    remember = BooleanField('Remeber me')
    submit = SubmitField(label='Log in')
