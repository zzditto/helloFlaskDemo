# author:LWZ
# datetime:2021/2/18 17:21

"""
文件说明：

"""
from jinja2.utils import generate_lorem_ipsum
from flask import Flask, session, url_for, redirect, request, abort

app = Flask(__name__)
app.secret_key = "secret key"


@app.route("/post")
def show_post():
    post_body = generate_lorem_ipsum(n=2)  # 生成两段随机文本
    return """
        <h1>A very long post</h1>
    <div class="body">%s</div>
    <button id="load">Load more</button>
    <script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script>
    <script type="text/javascript">
        $(function () {
            $('#load').click(function () {
                $.ajax({
                    url: "/more",
                    type: "get",
                    success: function (data) {
                        $('.body').append(data)
                    }
                })
            })
        })
    </script>
    """%post_body


@app.route("/more")
def load_post():
    return generate_lorem_ipsum(n=1)
