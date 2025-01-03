from spotdl.download.downloader import Downloader

# Test initialization of the Downloader class
downloader = Downloader(settings={
    'audio_providers': ['youtube'],
    'output': './downloads'  # Specify where to store downloaded songs
})

def search_song(song_name):
    try:
        song = downloader.search(song_name)
        return song  # Return the result
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    song = search_song("Never Gonna Give You Up")
    print(song)  # This will print the search result
