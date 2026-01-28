#!/bin/bash

echo "🚀 Setting up your Research Environment..."

# 1. Initialize/Sync the Python environment using uv
if command -v uv &> /dev/null; then
    uv sync
else
    echo "❌ Error: 'uv' is not installed. Please install it first."
    exit 1
fi

# 2. Create the hidden .git/hooks directory if it doesn't exist
HOOK_DIR=".git/hooks"
mkdir -p "$HOOK_DIR"

# 3. Create the pre-commit hook silently
cat << 'EOF' > "$HOOK_DIR/pre-commit"
#!/bin/bash
# Silently validate history before every commit
python3 history_manager.py > /dev/null 2>&1

# If validation fails, then we show the student the guide
if [ $? -ne 0 ]; then
    echo ""
    echo "⚠️  [Notice] We found a small formatting error in your tutor logs."
    echo "To fix it automatically, please run these two commands:"
    echo "  1. mv query_history_cleaned.jsonl query_history.jsonl"
    echo "  2. git add query_history.jsonl"
    echo ""
    exit 1
fi
exit 0
EOF

# 4. Make the hook executable
chmod +x "$HOOK_DIR/pre-commit"

# 5. Ensure the log file exists so the first run doesn't error
touch query_history.jsonl

echo "✅ Setup complete! You can now start your session with:"
echo "   uv run python_rag.py"