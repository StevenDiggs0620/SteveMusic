from flask import Flask, request, jsonify
from spotdl import Spotdl

app = Flask(__name__)

# Initialize Spotdl with necessary credentials
spotdl = Spotdl(client_id='your-client-id', client_secret='your-client-secret')

@app.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('query', '')  # Get search query from URL parameters
    if not search_term:
        return jsonify({'error': 'No search query provided'}), 400

    try:
        songs = spotdl.search([search_term])
        if not songs:
            return jsonify({'error': 'No songs found'}), 404

        song = songs[0]  # Use the first song in the list for now
        return jsonify({
            'song_name': song.display_name,
            'artists': song.artists,
            'album_name': song.album_name,
            'url': song.url,
            'cover_url': song.cover_url
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
