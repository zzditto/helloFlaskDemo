# author:LWZ
# datetime:2021/2/18 15:48

"""
文件说明：

"""
from flask import Flask, session, url_for, redirect, request, abort
from urllib.parse import urlparse, urljoin

app = Flask(__name__)
app.secret_key = "secret key"


@app.route("/")
@app.route("/hello")
def hello():
    name = request.args.get("name")
    if name is None:
        name = request.cookies.get("name", 'Human')
        response = f'<h1>hello,{name}</h1>'

    if 'log_in' in session:
        response += '[Authenticated]'
    else:
        response += '[Not Authenticated]'

    return response


@app.route("/admin")
def admin():
    if 'log_in' not in session:
        abort(403)
    return 'welcome to admin page'


@app.route("/login")
def login():
    session['log_in'] = True
    return redirect(url_for('hello'))


@app.route("/logout")
def logout():
    if 'log_in' in session:
        session.pop('log_in')

    return redirect(url_for("hello"))


def is_safe_url(target):
    print("host_url:"+request.host_url)
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    print("schema:"+test_url.scheme)
    print("netloc:"+ref_url.netloc)
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def redicect_back(default='hello'):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)

    return redirect(url_for(default))


@app.route("/foo")
def foo():
    return f"""<h1>Foo page</h1><a href="{url_for('do_somthing', next=request.full_path)}">Do something</a>"""


@app.route("/bar")
def bar():
    return f"""<h1>Bar page</h1><a href="{url_for('do_somthing', next=request.full_path)}">Do something</a>"""


@app.route("/do-somthing")
def do_somthing():
    return redicect_back()
