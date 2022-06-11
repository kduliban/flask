from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')

@app.route('/mypage')


@app.route('/mypage/me')
def info():

    return render_template("me.html", infos=infos)

@app.route('/mypage/contact', methods=['POST'])
def contact():
    print(request.form)
    return render_template("contact.html")


