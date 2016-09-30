# Flask
from flask import Flask, request, send_from_directory
app = Flask(__name__, static_folder='static', static_url_path='')

# Python
import sys
from os.path import join, dirname, abspath
ROOT = abspath(dirname(__file__))

# Templates (jinja)
from jinja2 import Template, Environment, FileSystemLoader

# Environment
jinja_env = Environment(loader=FileSystemLoader(join(ROOT, 'templates')))
#context = dict(users=users, articles=articles, page_navigation=navigation)
context = None

urls_dict = {
  'support'       : 'https://docs.google.com/forms/d/1kClxRpuObCe-dm4LR_d5qb2vJjyEf1DfbYOmDwMqzoA/viewform',
  'newsletter'    : 'https://goo.gl/forms/Dn9sCsVquh',
  'app_itunes'    : 'https://itunes.apple.com/us/app/gsdfaster-gtd-todo-lists-pomodoro/id488633128?mt=8',
  'app_itunes_gtd': 'https://itunes.apple.com/us/app/gtdfaster-free-todo-list-task/id498872399?mt=8'
}

# ===============================
# Routes - Media
@app.route('/media/<path:path>')
def send_media(path):
    return send_from_directory(app.static_folder, path)

# ===============================
# Robots & Sitemap
@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

# ===============================
# Routes - URLs (Core)
@app.route("/")
def page_homepage():
    template = jinja_env.get_template('index.html')
    content = {'page_id': 'home', 'urls_dict': urls_dict}
    return template.render(content)

# Core pages
@app.route("/about/")
@app.route("/contact/")
@app.route("/blog/")
@app.route("/videos/")
def page_generic():
    template_name = request.path.replace('/', '')
    template = jinja_env.get_template('{0}.html'.format(template_name))
    content = {'page_id': template_name, 'urls_dict': urls_dict, 'request_url': request.url}
    return template.render(content)

# Blog posts only
# How to use app features
@app.route("/blog/priority-urgent-vs-important/")
@app.route("/blog/gtd-context-location/")
@app.route("/blog/touchid-fingerprint-identity/")
@app.route("/blog/icloud-drive-sync-backup/")
@app.route("/blog/email-share-notes/")
@app.route("/blog/dwight-eisenhowers-urgency-importance-decision-matrix/")
@app.route("/blog/native-calendar-sync/")
@app.route("/blog/infinity-save-collect-even-faster/")
# On Productivity & GTD
@app.route("/blog/focus/")
@app.route("/blog/psychology-gtd-tools/")
@app.route("/blog/pomodoro-technique/")
@app.route("/blog/gtd-method-getting-things-done/")
@app.route("/blog/jz-rating-language-advisor-aglorithm/")
# Random notes
@app.route("/blog/getting-started-guide/")
@app.route("/blog/gsdfaster-vs-gtdfaster/")
@app.route("/blog/customer-testimonials-dec2015-jan2016/")
@app.route("/blog/get-app-version/")
@app.route("/blog/apple-watch-gtd-pomodoro/")
@app.route("/blog/your-new-superpowers/")
@app.route("/blog/reporting-bugs/")
@app.route("/blog/app-economy/")
def page_blog():
    template_name = request.path[1:len(request.path)-1]
    template = jinja_env.get_template('{0}.html'.format(template_name))
    content = {'page_id': template_name, 'urls_dict': urls_dict, 'request_url': request.url}
    return template.render(content)

# ===============================
@app.errorhandler(500)
def internal_error(error):
    template = Template('errorhandler: {{ error_msg }}!')
    template.render(error_msg=error)


# ===============================
# Main
# ===============================
if __name__ == "__main__":
    #app.run(debug=True)
    app.run()
