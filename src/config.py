from pathlib import Path

SESSION_GAP = 600
MIN_PLAY_MS = 30000
ROOT = Path(__file__).resolve().parent.parent 
RAW_DIR = ROOT / "data" / "raw"
INTERIM_DIR = ROOT / "data" / "interim"
PROCESSED_DIR = ROOT / "data" / "processed"

STREAMS_CSV = INTERIM_DIR / "streams.csv"
SESSIONS_CSV = PROCESSED_DIR / "sessions.csv"

MODEL_PATH = PROCESSED_DIR / "w2v.model"
CLUSTERS_PATH = PROCESSED_DIR / "clusters.csv"