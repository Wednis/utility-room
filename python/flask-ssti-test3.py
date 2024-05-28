#有点粗糙，随便做的，想加什么过滤就自己改代码，下一版本是直接页面选就行
from flask import *

app = Flask(__name__)

@app.errorhandler(500)
def internal_server_error(e):
    input_text = request.args.get('s')
    button1 = request.args.get('button1')    #按钮1，以此类推
    button2 = request.args.get('button2')
    button3 = request.args.get('button3')

    input_form = '<form action="/" method="get">'
    input_form += '<h3>请输入代码:</h3>'
    input_form += '<input type="text" id="input_text" name="s" value="{{input_text}}" style="width: 1600px; height: 40px; font-size: 20px;">'
    input_form += '<br>'
    input_form += '<label><input type="checkbox" name="button1" value="1" {0}> 关键字符串</label>'.format('checked' if button1 == "1" else '')
    input_form += '<label><input type="checkbox" name="button2" value="2" {0}> 关键字符</label>'.format('checked' if button2 == "2" else '')
    input_form += '<br>'
    input_form += '<input type="submit" value="提交">'
    input_form += '</form>'

    echo_content1 = '<p>原代码:<br>{{input_text}}</p>'
    echo_content2 = '<p>执行结果:<br>代码存在错误</p>'

    html = '<h1>Welcome to SSTI Test</h1>'
    html += input_form
    html += echo_content1
    html += echo_content2

    return render_template_string(html, input_text=input_text)

@app.route('/')
def index():
    input_text = request.args.get('s')
    button1 = request.args.get('button1')    #按钮1，以此类推
    button2 = request.args.get('button2')
    button3 = request.args.get('button3')

    input_form = '<form action="/" method="get">'
    input_form += '<h3>请输入代码:</h3>'
    input_form += '<input type="text" id="input_text" name="s" value="{{input_text}}" style="width: 1600px; height: 40px; font-size: 20px;">'
    input_form += '<br>'
    input_form += '<label><input type="checkbox" name="button1" value="1" {0}> 关键字符串</label>'.format('checked' if button1 == "1" else '')    #保持状态
    input_form += '<label><input type="checkbox" name="button2" value="2" {0}> 关键字符</label>'.format('checked' if button2 == "2" else '')
    input_form += '<br>'
    input_form += '<input type="submit" value="提交">'
    input_form += '</form>'

    echo_content1 = ''
    echo_content2 = ''

    #关键字符串
    blacklist1 = ["class"]
    #关键字符
    blacklist2 = ["[", "]"]


    if input_text:
        echo_content1 = '<p>原代码:<br>{{input_text}}</p>'       #无ssti处
        echo_content2 = '<p>执行结果:<br>%s</p>'%(input_text)    #存在ssti处

    if button1 == "1":
        for i in blacklist1:
            if i in input_text:
                echo_content2 = '<p>执行结果:<br>绕过过滤失败'

    if button2 == "2":
        for i in blacklist2:
            if i in input_text:
                echo_content2 = '<p>执行结果:<br>绕过过滤失败'

    html = '<h1>Welcome to SSTI Test</h1>'
    html += input_form
    html += echo_content1
    html += echo_content2

    return render_template_string(html, input_text=input_text)

if __name__ == '__main__':
    app.run()
