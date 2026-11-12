import pandas as pd 
from src.config import SESSIONS_CSV, MODEL_PATH
from gensim.models import Word2Vec

def train_model():
    streams = pd.read_csv(SESSIONS_CSV)
    sesh_list = streams.groupby("session_num")["spotify_track_uri"].agg(list).tolist() #first turn every bucket into list then turn whole series into list
    model = Word2Vec(sentences = sesh_list, vector_size = 32, window = 5, min_count = 2, sg = 1, seed = 42, epochs = 30, workers = 1)

    return model

if __name__ == "__main__":
    model = train_model()
    model.save(str(MODEL_PATH)) #gensim older than pathlib
