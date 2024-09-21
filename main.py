from config import PLAYLIST_ID
from spotify_auth import get_spotify_client
from playlist_manager import clear_playlist, add_tracks_to_playlist
from trend_analyzer import get_top_tracks, get_recommendations
#from listening_time_tracker import update_listening_time

def main():
    sp = get_spotify_client()
    
    # Update listening time before clearing the playlist
    #update_listening_time(sp, PLAYLIST_ID)
    
    # Clear the playlist
    clear_playlist(sp, PLAYLIST_ID)
    
    # Get the most listened track from the past 5 days
    most_listened_5_days = get_top_tracks(sp, time_range=5, limit=1)
    
    # Get the top 5 tracks from the past 2 days
    top_5_2_days = get_top_tracks(sp, time_range=2, limit=5)
    
    # Get recommendations based on recent listening history
    seed_tracks = get_top_tracks(sp, time_range=7, limit=5)
    recommended_tracks = get_recommendations(sp, seed_tracks, limit=44)  # 50 - 1 - 5 = 44
    
    # Combine all tracks
    playlist_tracks = most_listened_5_days + top_5_2_days + recommended_tracks
    
    # Add tracks to the playlist
    add_tracks_to_playlist(sp, PLAYLIST_ID, playlist_tracks)
    
    print("Playlist updated successfully!")
    print(f"First track: Most listened in past 5 days")
    print(f"Next 5 tracks: Top tracks from past 2 days")
    print(f"Remaining tracks: Based on listening preferences from past week")

if __name__ == "__main__":
    main()