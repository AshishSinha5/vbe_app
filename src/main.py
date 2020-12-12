import os
import sys
import webbrowser
from threading import Timer
from flask import Flask, render_template, request, url_for

sys.path.append('../')

from src.vbe_fci.fci import fci_util
from src.vbe_fci.vbe import vbe_util

app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def index():
    fci_text = ''
    fci_message = ''
    vbe_text = ''
    vbe_message = ''
    if request.method == 'POST':
        if request.form['submit'] == 'submit_fci_string':
            fci_text = request.form['string_fci']
            fci_message = fci_util(fci_text)

        if request.form['submit'] == 'submit_vbe_string':
            vbe_text = request.form['string_vbe']
            vbe_message = vbe_util(vbe_text)
    return render_template('index.html', fci_text=fci_text, fci_message=fci_message,
                           vbe_text=vbe_text, vbe_message=vbe_message)


'''
@app.route('/result', methods=['POST, GET'])
def result():
    if request.method == 'POST':
        fci_result = request.form
        return render_template("result.html", result=fci_result)
'''


def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')


if __name__ == '__main__':
    # print(os.path.dirname(os.path.realpath(__file__)))
    Timer(1, open_browser).start();
    app.run(debug=True)
