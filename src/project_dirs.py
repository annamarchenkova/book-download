import os
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = os.path.join(PROJECT_DIR, "output")
