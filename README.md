# SpotifyPlaylistMaker
Run everytime you want to update your playlist according to your recent listening trends 
Records data about listening trends to compare to old variations of the playlist 
pip install -r requirements.txt to run this project
After this create a .env file:
The .env file containing sensitive information (API keys, etc.) is not included in your repository (since it's ignored by .gitignore). You'll need to manually create this file on the new computer.
File setup(copy and paste, then fill in):
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
PLAYLIST_ID=your_playlist_id


