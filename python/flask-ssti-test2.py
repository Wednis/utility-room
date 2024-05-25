#进行更改，使得500错误时不会跳转（同时简化为一个文件（其实是复制粘贴哈哈）），可以测试过滤手段能否执行，下一版本应该是支持过滤或支持自选过滤
from flask import *

app = Flask(__name__)

@app.errorhandler(500)
def internal_server_error(e):
    input_text = request.args.get('s')

    input_form = '<form action="/" method="get">'
    input_form += '<h3>请输入代码:</h3>'
    input_form += '<input type="text" id="input_text" name="s" value="{{input_text}}" style="width: 1600px; height: 40px; font-size: 20px;">'
    input_form += '<input type="submit" value="提交">'
    input_form += '</form>'

    echo_content1 = '<p>原代码:<br>{{input_text}}</p>'
    echo_content2 = '<p>执行结果:<br>代码存在错误</p>'

    html = '<h1>Welcome to SSTI Test</h1>'
    html += input_form
    html += echo_content1
    html += echo_content2

    return render_template_string(html,input_text=input_text)

@app.route('/')
def index():
    input_text = request.args.get('s')

    input_form = '<form action="/" method="get">'
    input_form += '<h3>请输入代码:</h3>'
    input_form += '<input type="text" id="input_text" name="s" value="{{input_text}}" style="width: 1600px; height: 40px; font-size: 20px;">'
    input_form += '<input type="submit" value="提交">'
    input_form += '</form>'

    echo_content1 = ''
    echo_content2 = ''
    if input_text:
        echo_content1 = '<p>原代码:<br>{{input_text}}</p>'       #无ssti处
        try:
            input_text
            echo_content2 = '<p>执行结果:<br>%s</p>'%(input_text)    #存在ssti处            
        except:
            echo_content2 = '<p>执行结果:<br>代码存在错误</p>'

    html = '<h1>Welcome to SSTI Test</h1>'
    html += input_form
    html += echo_content1
    html += echo_content2

    return render_template_string(html,input_text=input_text)

if __name__ == '__main__':
    app.run()
