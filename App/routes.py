from flask import Blueprint, render_template, Response

main = Blueprint('main', __name__)

SITE_URL = 'https://benbarakwine.com'

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

@main.route('/robots.txt')
def robots():
    return Response(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n",
        mimetype='text/plain'
    )

@main.route('/sitemap.xml')
def sitemap():
    pages = ['', '/projects', '/vintages', '/curation', '/about', '/contact']
    urls = ''.join(
        f"<url><loc>{SITE_URL}{p}</loc></url>" for p in pages
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f'{urls}</urlset>'
    )
    return Response(xml, mimetype='application/xml')
