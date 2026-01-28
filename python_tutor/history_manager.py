import json
import sys
from pathlib import Path
from pydantic import BaseModel, ValidationError
from typing import Optional

class HistoryEntry(BaseModel):
    timestamp: str
    query: str
    response: str
    response_length: int
    model: str
    session_duration: Optional[float] = None  # New: Tracked in minutes

def validate_and_repair_history(file_path: str = "query_history.jsonl") -> bool:
    path = Path(file_path)
    if not path.exists(): return True
    valid_entries, errors = [], False
    with open(path, 'r') as f:
        for line in f:
            if not line.strip(): continue
            try:
                valid_entries.append(HistoryEntry(**json.loads(line)))
            except (json.JSONDecodeError, ValidationError):
                errors = True
    if errors:
        with open(path.stem + "_cleaned.jsonl", 'w') as f:
            for entry in valid_entries:
                f.write(entry.model_dump_json() + "\n")
        return False
    return True

if __name__ == "__main__":
    success = validate_and_repair_history()
    sys.exit(0 if success else 1)