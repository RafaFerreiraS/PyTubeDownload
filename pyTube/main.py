from flask import Flask, render_template, request, redirect
from pytube import YouTube

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    diretorio = request.form['dir'].replace('/', '//')
    video = YouTube(url)
    video.streams.get_highest_resolution().download(diretorio)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
