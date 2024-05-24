#用于本地测试ssti的代码，适用于新手
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    input_text = request.args.get('s')

    input_form = '<form action="/" method="get">'
    input_form += '<label for="input_text">请输入内容：</label>'
    input_form += '<input type="text" id="input_text" name="s" value="{}">'.format(input_text)
    input_form += '<input type="submit" value="提交">'
    input_form += '</form>'

    echo_content1 = ''
    echo_content2 = ''
    if input_text:
        echo_content1 = '<p>原命令:{{input_text}}</p>'
        echo_content2 = '<p>执行结果:%s</p>'%(input_text)

    html = '<h1>Welcome</h1>'
    html += input_form
    html += echo_content1
    html += echo_content2

    return render_template_string(html,input_text=input_text)

if __name__ == '__main__':
    app.run()
