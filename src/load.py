import pandas as pd
from src.config import RAW_DIR, INTERIM_DIR

def load_data() -> pd.DataFrame: 
    files = RAW_DIR.glob("*.json")
    streams = pd.concat([pd.read_json(file) for file in files])

    streams = streams.rename(columns={"master_metadata_track_name": "track_name"})
    streams = streams.rename(columns={"master_metadata_album_artist_name": "artist_name"})
    streams = streams.rename(columns={"master_metadata_album_album_name": "album_name"})

    streams = streams.loc[:, ["ts", "ms_played", "spotify_track_uri","track_name", "artist_name", "album_name"]]

    streams["ts"] = streams["ts"].map(lambda p: pd.to_datetime(p))
    return streams 

if __name__ == "__main__":
    streams = load_data()
    path = INTERIM_DIR / "streams.csv"
    streams.to_csv(path, index=False)
