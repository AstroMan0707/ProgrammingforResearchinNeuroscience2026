# These just work better cause they don't need a kernel

import os
from pathlib import Path
from datetime import datetime

# Create isolated practice directory with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
practice_dir = Path(f'/tmp/git_practice_{timestamp}')
practice_dir.mkdir(exist_ok=True)
os.chdir(practice_dir)

print(f"✓ Practice environment created: {practice_dir}")
print(f"✓ Current directory: {os.getcwd()}")
print("\n🎓 Safe to experiment - this is isolated from your real work!")