from pathlib import Path

SESSION_GAP = 600
MIN_PLAY_MS = 30000
ROOT = Path(__file__).resolve().parent.parent 
RAW_DIR = ROOT / "data" / "raw"
INTERIM_DIR = ROOT / "data" / "interim"
PROCESSED_DIR = ROOT / "data" / "processed"