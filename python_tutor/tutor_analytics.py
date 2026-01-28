import pandas as pd
import matplotlib.pyplot as plt
<<<<<<< HEAD
<<<<<<< HEAD
import matplotlib.dates as mdates
=======
>>>>>>> bbf1a83 (created functional rag agent python tutor)
=======
<<<<<<< HEAD
>>>>>>> 80cb1b4 (created functional rag agent python tutor)
=======
>>>>>>> c6a8249 (created functional rag agent python tutor)
>>>>>>> 46cbb68 (created functional rag agent python tutor)
import seaborn as sns
import json
import re
from pathlib import Path
from collections import Counter
<<<<<<< HEAD
<<<<<<< HEAD
import datetime
=======
import date
<<<<<<< HEAD
>>>>>>> 80cb1b4 (created functional rag agent python tutor)
=======
>>>>>>> c6a8249 (created functional rag agent python tutor)
>>>>>>> 46cbb68 (created functional rag agent python tutor)

# Use a clean, professional style for colleagues
sns.set_theme(style="whitegrid", context="talk")
<<<<<<< HEAD
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
=======
import date

# Use a clean, professional style for colleagues
# Use a clean, professional style for colleagues
sns.set_theme(style="whitegrid", context="talk")
TARGET_KEYWORDS = ["tuple", "unpacking", "list", "class", "function", "scope", "decorator"]
>>>>>>> bbf1a83 (created functional rag agent python tutor)
=======
TARGET_KEYWORDS = ["tuple", "unpacking", "list", "class", "function", "scope", "decorator"]
<<<<<<< HEAD
>>>>>>> 80cb1b4 (created functional rag agent python tutor)
=======
>>>>>>> c6a8249 (created functional rag agent python tutor)
>>>>>>> 46cbb68 (created functional rag agent python tutor)

def generate_visualizations(file_path: str = "query_history.jsonl"):
    path = Path(file_path)
    if not path.exists():
<<<<<<< HEAD
<<<<<<< HEAD
        print("No history file found.")
        return

    # 1. Load and Parse Data
=======
        print("No history file found to analyze.")
        return

    # 1. Load Data
>>>>>>> bbf1a83 (created functional rag agent python tutor)
=======
        print("No history file found to analyze.")
        return

    # 1. Load Data
<<<<<<< HEAD
>>>>>>> 80cb1b4 (created functional rag agent python tutor)
=======
>>>>>>> c6a8249 (created functional rag agent python tutor)
>>>>>>> 46cbb68 (created functional rag agent python tutor)
    data = []
    with open(path, 'r') as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
<<<<<<< HEAD
<<<<<<< HEAD
    
    # 2. Aggregating Data
    # Group by date and SUM the session_duration for a true daily total
    daily_engagement = df.groupby(df['timestamp'].dt.date)['session_duration'].sum().reset_index()
    daily_engagement.columns = ['date', 'total_minutes']
=======
    df['date'] = df['timestamp'].dt.date
<<<<<<< HEAD
>>>>>>> 80cb1b4 (created functional rag agent python tutor)
=======
>>>>>>> c6a8249 (created functional rag agent python tutor)
>>>>>>> 46cbb68 (created functional rag agent python tutor)

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
<<<<<<< HEAD
    print(f"✅ Professional report saved: {output_name}")
=======
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
        ax2.text(0.5, 0.5, "No keywords detected yet", ha='center')

    # Save and Show
    # Save and Show
    output_name = "tutor_analytics_report.png"
    plt.savefig(output_name, bbox_inches='tight', dpi=300)
    print(f"✅ High-quality report saved as: {output_name}")
>>>>>>> bbf1a83 (created functional rag agent python tutor)
=======
    print(f"✅ High-quality report saved as: {output_name}")
<<<<<<< HEAD
>>>>>>> 80cb1b4 (created functional rag agent python tutor)
=======
>>>>>>> c6a8249 (created functional rag agent python tutor)
>>>>>>> 46cbb68 (created functional rag agent python tutor)
    plt.show()

if __name__ == "__main__":
    generate_visualizations()