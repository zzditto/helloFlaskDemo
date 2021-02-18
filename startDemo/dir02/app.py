# author:LWZ
# datetime:2021/2/18 22:28

"""
文件说明：
"""

from flask import Flask, render_template

app = Flask(__name__)

user = {
    'username': 'Grey Li',
    'bio': 'A boy who loves movies and music.',
}
movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]


@app.route("/")
def index():
    return render_template('index.html', user=user, movies=movies)


@app.context_processor
def inject_foo():
    foo = "I'm foo"
    return dict(foo=foo)


@app.template_global
def bar():
    return "I am bar"


from flask import Markup


@app.template_filter()
def custom_filter(s):
    return s + Markup("hello")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404
