import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import re
from pathlib import Path
from collections import Counter
import date

# Use a clean, professional style for colleagues
sns.set_theme(style="whitegrid", context="talk")
TARGET_KEYWORDS = ["tuple", "unpacking", "list", "class", "function", "scope", "decorator"]

def generate_visualizations(file_path: str = "query_history.jsonl"):
    path = Path(file_path)
    if not path.exists():
        print("No history file found to analyze.")
        return

    # 1. Load Data
    data = []
    with open(path, 'r') as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date

    # Create the figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 14))
    plt.subplots_adjust(hspace=0.4)

    # --- Plot 1: Total Engagement (Time Series) ---
    # Aggregate total session duration per day
    daily_engagement = df.groupby('date')['session_duration'].max().reset_index()
    
    sns.lineplot(data=daily_engagement, x='date', y='session_duration', 
                 marker='o', color='#2c3e50', linewidth=2.5, ax=ax1)
    ax1.set_title("Student Engagement Over Time", pad=20, fontweight='bold')
    ax1.set_xlabel("Date", fontsize=14)
    ax1.set_ylabel("Total Session Time (Minutes)", fontsize=14)
    ax1.tick_params(axis='x', rotation=45)

    # --- Plot 2: Keyword Frequency Boxplot ---
    # We create a distribution of how often keywords appear across all interactions
    keyword_data = []
    for _, row in df.iterrows():
        text = f"{row['query']} {row['response']}".lower()
        for word in TARGET_KEYWORDS:
            count = len(re.findall(rf'\b{word}\b', text))
            if count > 0:
                keyword_data.append({"Keyword": word, "Mentions": count})
    
    if keyword_data:
        kw_df = pd.DataFrame(keyword_data)
        sns.boxplot(data=kw_df, x='Keyword', y='Mentions', palette="viridis", ax=ax2)
        ax2.set_title("Concept Engagement Distribution", pad=20, fontweight='bold')
        ax2.set_xlabel("Python Concept", fontsize=14)
        ax2.set_ylabel("Frequency per Interaction", fontsize=14)
    else:
        ax2.text(0.5, 0.5, "No keywords detected yet", ha='center')

    # Save and Show
    output_name = "tutor_analytics_report.png"
    plt.savefig(output_name, bbox_inches='tight', dpi=300)
    print(f"✅ High-quality report saved as: {output_name}")
    plt.show()

if __name__ == "__main__":
    generate_visualizations()