from flask import Flask, render_template, request, send_file
from downloader import download_video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    quality = request.form['quality']
    
    # Download the video
    filename = download_video(url, quality)
    
    # Send the file back as a response for download
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
