from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return send_from_directory('.', 'index.html')


@app.route('/about')
def about():
    return send_from_directory('.', 'about.html')


@app.route('/blog')
def blog():
    return send_from_directory('.', 'blog.html')


@app.route('/contact')
def contact():
    return send_from_directory('.', 'contact.html')


@app.route('/faq')
def faq():
    return send_from_directory('.', 'faq.html')


@app.route('/services')
def services():
    return send_from_directory('.', 'services.html')


@app.route('/404')
def error_404():
    return send_from_directory('.', '404.html')


if __name__ == '__main__':
    app.run(debug=True)
