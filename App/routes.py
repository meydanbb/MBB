from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/projects')
def projects():
    return render_template('projects.html')

@main.route('/curation')
def curation():
    return render_template('curation.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/vintages')
def vintages():
    return render_template('vintages.html')
