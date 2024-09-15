def clear_playlist(sp, playlist_id):
    print(f"Playlist ID: {playlist_id}") #error check
    sp.playlist_replace_items(playlist_id, [])
    print(f"Cleared Playlist: {playlist_id}")

def add_tracks_to_playlist(sp, playlist_id, track_ids):
    sp.playlist_add_items(playlist_id, track_ids)
    print(f"Added {len(track_ids)} tracks to playlist: {playlist_id}")
    


