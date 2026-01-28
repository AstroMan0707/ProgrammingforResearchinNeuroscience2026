import json
import re
from pathlib import Path
from collections import Counter

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

def display_cli_metrics(file_path: str = "query_history.jsonl", duration: float = 0.0):
    path = Path(file_path)
    if not path.exists(): return
    
    interactions = [json.loads(line) for line in open(path) if line.strip()]
    if not interactions: return

    # Track STUDENT keywords only by ignoring 'response'
    student_queries = [i['query'].lower() for i in interactions]
    all_student_text = " ".join(student_queries)
    
    keyword_counts = Counter({
        w: len(re.findall(rf'\b{w}\b', all_student_text)) 
        for w in TARGET_KEYWORDS if len(re.findall(rf'\b{w}\b', all_student_text)) > 0
    })

    print("\n" + "="*50)
    print("      CUMULATIVE TUTORING INSIGHTS")
    print("="*50)
    print(f"Session Duration:  {duration} minutes")
    print(f"Total Queries:     {len(interactions)}")
    print(f"Avg Tutor Length:  {sum(i['response_length'] for i in interactions)/len(interactions):.1f} chars")
    print("-" * 50)
    
    print("Top Student Concepts (Total Count):")
    if not keyword_counts:
        print("  No tracked keywords identified yet.")
    else:
        for word, count in keyword_counts.most_common(5):
            print(f"  {word.ljust(12)} | {'●' * count} ({count})")
    
    # IMPROVED: Scaled Activity Volume
    print("\nRecent Activity (Last 5 Responses):")
    MAX_BAR_WIDTH = 30 
    # Use 2000 chars as a standard "long" response for scaling
    for i, entry in enumerate(interactions[-5:]):
        raw_len = entry['response_length']
        # Normalize: ensure the bar never exceeds MAX_BAR_WIDTH
        scaled_len = min(int((raw_len / 2000) * MAX_BAR_WIDTH), MAX_BAR_WIDTH)
        bar = '█' * scaled_len
        # Print actual length as a number for precision
        print(f"  Q{i+1}: {bar.ljust(MAX_BAR_WIDTH)} | {raw_len} chars")
    
    print("="*50 + "\n")

if __name__ == "__main__":
    display_cli_metrics()