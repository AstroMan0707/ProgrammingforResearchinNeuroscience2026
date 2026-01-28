import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import json
import re
from pathlib import Path
from collections import Counter
import datetime

# Professional styling for colleagues
sns.set_theme(style="whitegrid", context="talk")
TARGET_KEYWORDS = ["tuple", "unpacking", "list", "class", "function", "scope", "decorator", "variable", "loop", "dictionary",
                   "string", "integer", "float", "boolean", "set", "module", "package", "exception", "file", "comprehension",
                   "lambda", "iterator", "generator", "recursion", "inheritance", "polymorphism", "encapsulation", "abstraction",
                   "method", "attribute", "namespace", "argument", "parameter", "default argument", "keyword argument",
                   "mutable", "immutable", "type hint", "virtual environment", "debugging", "testing", "OOP", "functional programming",
                   "data structure", "algorithm", "API", "library", "framework", "syntax", "semantics", "interpreter", "compiler",
                   "PEP8", "docstring", "decorator", "context manager", "with statement", "async", "await", "threading", "multiprocessing",
                   'git', 'github', 'version control', 'Jupyter', 'notebook', 'pandas', 'numpy', 'matplotlib', 'visualization',
                   'data analysis', 'data science', 'machine learning', 'AI', 'artificial intelligence', 'deep learning', 'neural network',
                   'tensorflow', 'pytorch', 'scikit-learn', 'regression', 'classification', 'clustering', 'natural language processing', 'NLP',
                   'Methods', 'Functions', 'Attributes', 'Classes', 'Objects'
                   ]

def generate_visualizations(file_path: str = "query_history.jsonl"):
    path = Path(file_path)
    if not path.exists():
        print("No history file found.")
        return

    # 1. Load and Parse Data
    data = []
    with open(path, 'r') as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # 2. Aggregating Data
    # Group by date and SUM the session_duration for a true daily total
    daily_engagement = df.groupby(df['timestamp'].dt.date)['session_duration'].sum().reset_index()
    daily_engagement.columns = ['date', 'total_minutes']

    # Aggregate Concept Mentions (Student Inquiries Only)
    concept_counts = Counter()
    for query in df['query'].astype(str).str.lower():
        for word in TARGET_KEYWORDS:
            count = len(re.findall(rf'\b{word}\b', query))
            if count > 0:
                concept_counts[word] += count

    kw_df = pd.DataFrame(list(concept_counts.items()), columns=['Concept', 'Total Mentions'])
    kw_df = kw_df.sort_values(by='Total Mentions', ascending=False)

    # 3. Create High-Quality Visualization
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 14))
    plt.subplots_adjust(hspace=0.5)

    # --- Plot 1: Daily Engagement (Cleaned Date Axis) ---
    sns.lineplot(data=daily_engagement, x='date', y='total_minutes', 
                 marker='o', color='#2c3e50', linewidth=3, ax=ax1)
    
    # CLEANING THE DATE AXIS:
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %d')) # Format as 'Jan 28'
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=1))    # Tick for every day
    
    ax1.set_title("Daily Student Engagement", pad=20, fontweight='bold', fontsize=20)
    ax1.set_ylabel("Total Minutes", fontsize=16)
    ax1.set_xlabel("Session Date", fontsize=16)

    # --- Plot 2: Concept Engagement (Professional Bar Chart) ---
    if not kw_df.empty:
        sns.barplot(data=kw_df, x='Concept', y='Total Mentions', palette="viridis", ax=ax2)
        ax2.set_title("Cumulative Concept Engagement", pad=20, fontweight='bold', fontsize=20)
        ax2.set_ylabel("Total Student Mentions", fontsize=16)
        ax2.set_xlabel("Python Concept", fontsize=16)
        ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='center')
    else:
        ax2.text(0.5, 0.5, "No target keywords detected.", ha='center')

    # Final Polish
    sns.despine()
    output_name = "tutor_analytics_report.png"
    plt.savefig(output_name, bbox_inches='tight', dpi=300)
    print(f"✅ Professional report saved: {output_name}")
    plt.show()

if __name__ == "__main__":
    generate_visualizations()