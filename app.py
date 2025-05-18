from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

# Override static file behavior to prevent 304
@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        filename,
        conditional=False  # <- disables 304
    )

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
