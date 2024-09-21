# trend_analyzer.py
from collections import Counter
from datetime import datetime, timedelta

def get_recent_tracks(sp, days=7):
    # Get tracks from the last 'days' days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    tracks = []
    results = sp.current_user_recently_played(limit=50)
    
    while results['items'] and datetime.strptime(results['items'][-1]['played_at'], '%Y-%m-%dT%H:%M:%S.%fZ') > start_date:
        for item in results['items']:
            played_at = datetime.strptime(item['played_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
            if start_date <= played_at <= end_date:
                tracks.append(item)
        
        if results['next']:
            results = sp.next(results)
        else:
            break
    
    return tracks

def analyze_trends(sp, tracks, time_range):
    track_counter = Counter()
    for track in tracks:
        played_at = datetime.strptime(track['played_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        if datetime.now() - played_at <= timedelta(days=time_range):
            track_counter[track['track']['id']] += 1
    
    return track_counter.most_common()

def get_top_tracks(sp, time_range, limit):
    tracks = get_recent_tracks(sp, days=time_range)
    top_tracks = analyze_trends(sp, tracks, time_range)
    return [track_id for track_id, _ in top_tracks[:limit]]

def get_recommendations(sp, seed_tracks, limit):
    recommendations = sp.recommendations(seed_tracks=seed_tracks, limit=limit)
    return [track['id'] for track in recommendations['tracks']]