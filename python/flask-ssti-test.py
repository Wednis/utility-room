#用于本地测试ssti的代码，适用于新手
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    input_text = request.args.get('s')

    input_form = '<form action="/" method="get">'
    input_form += '<h3>请输入代码:</h3>'
    input_form += '<input type="text" id="input_text" name="s" value="{{input_text}}" style="width: 1600px; height: 40px; font-size: 20px;">'
    input_form += '<input type="submit" value="提交">'
    input_form += '</form>'

    echo_content1 = '<p>(代码错误会产生500错误)</p>'
    echo_content2 = ''
    echo_content3 = ''
    if input_text:
        echo_content2 = '<p>原代码:<br>{{input_text}}</p>'       #无ssti处
        echo_content3 = '<p>执行结果:<br>%s</p>'%(input_text)    #存在ssti处

    html = '<h1>Welcome to SSTI Test</h1>'
    html += input_form
    html += echo_content1
    html += echo_content2
    html += echo_content3

    return render_template_string(html,input_text=input_text)

if __name__ == '__main__':
    app.run()
