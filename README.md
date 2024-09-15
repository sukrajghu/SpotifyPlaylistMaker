# SpotifyPlaylistMaker
Run everytime you want to update your playlist according to your recent listening trends <br/>
Records data about listening trends to compare to old variations of the playlist <br/>
pip install -r requirements.txt to run this project <br/>
After this create a .env file: <br/>
The .env file containing sensitive information (API keys, etc.) is not included in your repository (since it's ignored by .gitignore). You'll need to manually create this file on the new computer. <br/>
File setup(copy and paste, then fill in): <br/>
SPOTIPY_CLIENT_ID=your_spotify_client_id <br/>
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret <br/>
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback <br/>
PLAYLIST_ID=your_playlist_id <br/>


