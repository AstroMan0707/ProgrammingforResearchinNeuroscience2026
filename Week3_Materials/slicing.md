# Pandas Slicing: Syntax and Use Cases Reference Guide

Slicing is a powerful technique for extracting subsets of data from DataFrames. This guide covers the syntax and practical use cases for beginners.

---

## Core Slicing Methods

### 1. `.iloc[]` - Integer Location Based Slicing

**Syntax:**
```python
df.iloc[row_start:row_end, col_start:col_end]
```

**Key Points:**
- Uses **integer positions** (0-indexed)
- End index is **exclusive** (not included)
- Works like Python list slicing
- Cannot use row/column names

**Examples:**
```python
df.iloc[0:3]              # Rows 0, 1, 2
df.iloc[:5]               # First 5 rows
df.iloc[-3:]              # Last 3 rows
df.iloc[2:7, 0:3]         # Rows 2-6, columns 0-2
df.iloc[::2]              # Every other row
df.iloc[:, 1]             # All rows, column at index 1
df.iloc[[0, 2, 4]]        # Specific rows by position
```

**Use Cases:**
- Extract first/last N rows
- Get every nth row or column
- Select specific row/column ranges by position
- When you don't know column names

---

### 2. `.loc[]` - Label Based Slicing

**Syntax:**
```python
df.loc[row_label_start:row_label_end, col_name_start:col_name_end]
```

**Key Points:**
- Uses **row/column labels or names**
- End index is **inclusive** (included in result)
- Works with string indices, dates, or custom labels
- More readable when labels are meaningful

**Examples:**
```python
df.loc['row_a':'row_c']           # Rows 'row_a' through 'row_c' (inclusive)
df.loc[:, 'Age':'Score']          # All rows, columns 'Age' to 'Score'
df.loc['2024-01-01':'2024-01-10'] # Date range slicing
df.loc[['row_a', 'row_c']]        # Specific rows by label
df.loc['row_b', 'Age']            # Single cell
df.loc['row_a':, ['Name', 'Age']] # From row_a onward, specific columns
```

**Use Cases:**
- Work with meaningful row/column names
- Extract date ranges
- Slice when you know the labels
- More intuitive for labeled data

---

## Important Differences: `.iloc[]` vs `.loc[]`

| Feature | `.iloc[]` | `.loc[]` |
|---------|-----------|---------|
| Index Type | Integer position | Labels/names |
| End Behavior | Exclusive | Inclusive |
| Slicing Style | Python-like | Label-based |
| Use Case | Position-based | Label/name-based |

**Example:**
```python
df.iloc[1:4]    # Returns rows at index 1, 2, 3
df.loc[1:4]     # Returns rows with labels 1, 2, 3, 4
```

---

## Advanced Slicing Techniques

### 3. Boolean Indexing (Conditional Slicing)

**Syntax:**
```python
df[df['column'] > value]
df[df['column'].isin([val1, val2])]
df[(df['col1'] > x) & (df['col2'] < y)]
```

**Examples:**
```python
# Single condition
df[df['Age'] > 30]

# Multiple conditions (use & and |, NOT 'and'/'or')
df[(df['Age'] > 25) & (df['Score'] < 90)]

# Check membership
df[df['Department'].isin(['Sales', 'HR'])]

# String matching
df[df['Name'].str.contains('Alice')]
```

**Use Cases:**
- Filter rows based on conditions
- Find data matching specific criteria
- Exclude outliers or missing values

---

## Common Slicing Patterns

### Pattern 1: First/Last N Rows
```python
df.head(10)              # First 10 rows (built-in method)
df.tail(5)               # Last 5 rows (built-in method)
df.iloc[:10]             # First 10 rows
df.iloc[-5:]             # Last 5 rows
```

### Pattern 2: Specific Columns Only
```python
df[['Name', 'Age']]           # Multiple specific columns
df.iloc[:, [0, 2, 4]]         # Columns at positions 0, 2, 4
df.loc[:, 'Age':'Score']      # Column range
```

### Pattern 3: Date Range
```python
df.loc['2024-01-01':'2024-12-31']  # Full year
df.loc[:'2024-06-30']              # Up to June 30
df.loc['2024-03':, ]               # March 2024 onward
```

### Pattern 4: Exclude Rows
```python
df[~(df['Age'] > 50)]              # NOT condition
df[df['Status'] != 'Inactive']     # Not equal to
```

### Pattern 5: Rows with Missing Values
```python
df[df['column'].isna()]            # Find NaN values
df[df['column'].notna()]           # Exclude NaN values
df.dropna()                        # Remove all NaN rows
```

---

## Best Practices

### ✅ DO:
- Use `.iloc[]` when working with row/column positions
- Use `.loc[]` when working with labels or conditions
- Use boolean indexing for complex filtering
- Chain conditions clearly with parentheses
- Use `.head()` and `.tail()` for quick inspection

### ❌ DON'T:
- Mix `.iloc[]` and `.loc[]` syntax (end inclusivity differs)
- Use Python's `and`/`or` with boolean arrays; use `&`/`|` instead -- ('|' signifies 'or')
- Forget that `.loc[]` end index is **inclusive**
- Forget that `.iloc[]` end index is **exclusive**
- Slice without understanding your data structure first

---

## Performance Tips

1. **Use `.loc[]` with booleans** - Faster than filtering with loops
2. **Avoid chained indexing** - Use `.loc[]` or `.iloc[]` in one operation


```python
# Slow - chained indexing
df['Age'][df['Age'] > 30]

# Fast - single operation
df.loc[df['Age'] > 30, 'Age']
```

---

## Common Mistakes and Solutions

| Mistake | Solution |
|---------|----------|
| `df[df['Age'] > 30 and df['Score'] < 80]` | Use `&` not `and`: `df[(df['Age'] > 30) & (df['Score'] < 80)]` |
| `df.loc[0:5]` returns 6 rows | Remember `.loc[]` is inclusive! |
| `df.iloc[0:5]` returns only 5 rows | This is correct - `.iloc[]` is exclusive at end |
| `df[df.Age > 30]` attribute error | Use bracket notation: `df[df['Age'] > 30]` |
| Selecting a single row returns Series | Use double brackets for DataFrame: `df.loc[[0]]` vs `df.loc[0]` |

---

## Quick Reference Cheat Sheet

```python
# ROW SLICING
df.iloc[0:5]           # Rows 0-4 by position
df.loc['a':'d']        # Rows a-d by label (inclusive)
df[df['col'] > 5]      # Conditional rows

# COLUMN SLICING
df[['col1', 'col2']]   # Specific columns
df.iloc[:, 0:3]        # Columns 0-2 by position
df.loc[:, 'col1':'col3']  # Columns col1-col3 by label

# BOTH
df.loc['row1':'row3', 'col1':'col3']  # Rectangular region
df.iloc[0:3, 1:4]      # By position

# CONDITIONAL
df[df['Age'] > 30]           # Simple condition
df[(df['Age'] > 30) & (df['Score'] < 90)]  # Multiple
df[df['Name'].isin(['Alice', 'Bob'])]      # Membership
```

