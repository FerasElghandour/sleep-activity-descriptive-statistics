"""Offline example using the public implementation; see README for evidence scope."""
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
os.chdir(ROOT)

from describe import describe
# Fictional observations demonstrate calculation conventions only.
result = describe([1, 2, 3, 4])

import json
print(json.dumps(result, indent=2))

