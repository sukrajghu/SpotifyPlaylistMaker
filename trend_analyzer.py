def get_recent_tracks(sp):
    results = sp.current_user_recently_played(limit=50)
    return results['items']

def analyze_trends(sp, tracks):
    # This is a simplified analysis. 
    # make it more sophisticated later
    genres = {}
    artists = {}
    
    for track in tracks:
        artist_id = track['track']['artists'][0]['id']
        artist_info = sp.artist(artist_id)
        
        for genre in artist_info['genres']:
            genres[genre] = genres.get(genre, 0) + 1
        
        artist_name = track['track']['artists'][0]['name']
        artists[artist_name] = artists.get(artist_name, 0) + 1
    
    top_genres = sorted(genres.items(), key=lambda x: x[1], reverse=True)[:5]
    top_artists = sorted(artists.items(), key=lambda x: x[1], reverse=True)[:5]
    
    return top_genres, top_artists

def get_recommendations(sp, top_genres, top_artists):
    seed_genres = [genre for genre, _ in top_genres[:2]]
    seed_artists = [sp.search(q=artist, type='artist')['artists']['items'][0]['id'] for artist, _ in top_artists[:2]]
    
    recommendations = sp.recommendations(seed_genres=seed_genres, seed_artists=seed_artists, limit=30)
    return [track['id'] for track in recommendations['tracks']]
