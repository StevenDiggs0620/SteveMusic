from spotdl.download.downloader import Downloader

# Test initialization of the Downloader class
downloader = Downloader(settings={
    'audio_providers': ['youtube'],
    'output': './downloads'  # Specify where to store downloaded songs
})

def search_song(song_name):
    try:
        print(f"Searching for song: {song_name}")  # Log the search
        song = downloader.search(song_name)
        print(f"Song found: {song}")  # Log the result of the search
        return song  # Return the result
    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Log any errors
        return str(e)

if __name__ == '__main__':
    song = search_song("Never Gonna Give You Up")
    print(f"Search result: {song}")  # Final output of the search
