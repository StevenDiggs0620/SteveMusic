from flask import Flask, request, jsonify
from spotdl import SpotDL  # Assuming this imports your SpotDL code
from spotdl.download.downloader import Downloader

app = Flask(__name__)

# Initialize SpotDL
spot_dl = SpotDL()

@app.route('/search', methods=['GET'])
def search():
    song_name = request.args.get('song', '')
    if song_name:
        try:
            song_url = spot_dl.search(song_name)
            return jsonify({"url": song_url})
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "No song query provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
