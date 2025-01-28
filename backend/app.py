from flask import Flask, render_template, request, send_file
from downloader import download_video
import os

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
    # Use the PORT environment variable for the port and bind to 0.0.0.0
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT isn't set
    app.run(host='0.0.0.0', port=port, debug=True)
