import pandas as pd 
from src.config import SESSIONS_CSV, STREAMS_CSV, SESSION_GAP, MIN_PLAY_MS

def get_sessions():
    streams = pd.read_csv(STREAMS_CSV, parse_dates = ["ts"]) #make sure to parse the dates

    streams["differences"] = streams["ts"].diff().dt.total_seconds() - streams["ms_played"] / 1000
    # streams["differences"] = streams["differences"].map(lambda x: 0 if x < 0 else x)
    streams["differences"] = streams["differences"].clip(lower = 0) # same as above line
    streams["differences"] = streams["differences"].fillna(1000)

    streams["session_num"] = (streams["differences"] > SESSION_GAP).cumsum()
    streams = streams.loc[streams["ms_played"] > MIN_PLAY_MS] 

    session_counts = streams.groupby("session_num")["session_num"].transform("size")  #doesn't matter which column you apply transform(size) on 
    streams = streams.loc[(session_counts >= 2) & streams["spotify_track_uri"].notnull()]  
    return streams 

def get_tracks():
    streams = pd.read_csv(SESSIONS_CSV)
    # streams["label"] = streams["track_name"] + " - " + streams["artist_name"]
    tracks = streams.drop_duplicates("spotify_track_uri").set_index("spotify_track_uri").loc[:, ["track_name", "artist_name"]]
    play_count = streams.groupby("spotify_track_uri").size()
    return tracks, play_count

if __name__ == "__main__":
    sessions = get_sessions()
    sessions.to_csv(SESSIONS_CSV, index=False)
