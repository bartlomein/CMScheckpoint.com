from flask import Flask
from flask import render_template
from flask import request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from WordpressCheck import *


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'



class TextArea(FlaskForm):
    url_area = StringField('Enter a URL:', validators=[DataRequired()])
    submit = SubmitField('CHECK')




@app.route('/', methods=['GET', 'POST'])
def index():
    outcome = ''
    form = TextArea(request.form)

    if request.method == 'POST':
        name = request.form['url_area']
        outcome = checker(name)

    return render_template("index.html",outcome = outcome,  form=form )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
