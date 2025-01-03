from spotdl import Spotdl
from flask import Flask, jsonify

app = Flask(__name__)

# Set up SpotDL with your credentials
spotdl = Spotdl(client_id='your-client-id', client_secret='your-client-secret')

@app.route('/')
def home():
    return "Welcome to SteveMusic API"

@app.route('/search', methods=['GET'])
def search():
    try:
        # Replace with actual query or dynamically fetch from request
        song_query = ['joji - test drive', 'https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT']
        songs = spotdl.search(song_query)

        # Ensure the search results are not empty
        if not songs:
            return jsonify({'error': 'No songs found'}), 404

        # For now, we'll return the first song and its details
        song = songs[0]
        return jsonify({
            'song_name': song.display_name,
            'artist': song.artist,
            'url': song.url
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
