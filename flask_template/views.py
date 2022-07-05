from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template("index.html")

@my_view.route('/tilly')
def tilly():
    return render_template("tilly.html")


@my_view.route('/TILLYSPAGE')
@my_view.route('/tillyspage')
def tilly_redirect():
    return redirect(url_for("my_view.tilly"))