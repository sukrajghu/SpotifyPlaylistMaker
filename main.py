from config import PLAYLIST_ID
from spotify_auth import get_spotify_client
from playlist_manager import clear_playlist, add_tracks_to_playlist
from trend_analyzer import get_recent_tracks, analyze_trends, get_recommendations

def main():
    sp = get_spotify_client()
    
    # Clear the playlist
    clear_playlist(sp, PLAYLIST_ID)
    
    # Get recent tracks
    recent_tracks = get_recent_tracks(sp)
    
    # Analyze trends
    top_genres, top_artists = analyze_trends(sp, recent_tracks) 
    #diff variations with ot without sp as parameter
    print("Top Genres:", top_genres)
    print("Top Artists:", top_artists)
    
    # Get recommendations
    recommended_tracks = get_recommendations(sp, top_genres, top_artists)
    
    # Add new tracks to the playlist
    add_tracks_to_playlist(sp, PLAYLIST_ID, recommended_tracks)

if __name__ == "__main__":
    main()
