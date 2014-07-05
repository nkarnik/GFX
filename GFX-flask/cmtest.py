from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

from flask.ext.wtf import Form
from flask.ext.codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField

from flask.ext.codemirror import CodeMirror
import sys
from cStringIO import StringIO
import json


a = '' 

with open('bt1.py', 'r') as fi:
    a = fi.read()

print a

app = Flask(__name__)
app.config.from_object('config')
codemirror = CodeMirror(app)

# mandatory
CODEMIRROR_LANGUAGES = ['python', 'html']
# optional
CODEMIRROR_THEME = '3024-day'


class MyForm(Form):
    source_code = CodeMirrorField(language='python', config={'lineNumbers' : 'true'}, default=a)
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def cm():
    #code = request.form['source_code']

    #print code
    try:
        exec code

    except:
        pass
    form = MyForm()

    var = json.dumps([4])

    if form.validate_on_submit():
        text = form.source_code.data
    return render_template('cmtest.html', form = form, var = var)


@app.route('/result', methods = ['GET', 'POST'])
def cmr():
    code = request.form['source_code']
    out = ''

    var = '' 
    print code
    try:
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        exec(code)
        sys.stdout = old_stdout

        out = str(redirected_output.getvalue())
        out = out.split("%%%",1)[1]         
        print output
        backtest = output

    except:
        pass

    form = MyForm()
    var = json.dumps(var)

    if form.validate_on_submit():
        text = form.source_code.data
    return render_template('cmtest.html', form = form, var = output, res = out, run = True)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

