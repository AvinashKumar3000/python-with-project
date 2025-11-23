Here is a **clean, simple, beginner-friendly Pandas Cheat Sheet** — perfect for students and quick revision.

---

# 🔥 **Pandas Cheat Sheet (Python)**

---

# ✅ **1. Importing Pandas**

```python
import pandas as pd
```

---

# ✅ **2. Creating DataFrames**

### **From Dictionary**

```python
df = pd.DataFrame({
    "name": ["Avi", "John"],
    "age": [20, 25]
})
```

### **From List of Lists**

```python
df = pd.DataFrame([[1, 2], [3, 4]], columns=["A", "B"])
```

### **Read CSV**

```python
df = pd.read_csv("data.csv")
```

### **Write CSV**

```python
df.to_csv("output.csv", index=False)
```

---

# ✅ **3. Viewing Data**

```python
df.head()         # first 5 rows
df.tail()         # last 5 rows
df.info()         # summary
df.describe()     # statistics
df.shape          # rows, columns
```

---

# ✅ **4. Selecting Data**

### **Column**

```python
df["name"]
df[["name", "age"]]
```

### **Row index (iloc)**

```python
df.iloc[0]          # first row
df.iloc[0:3]        # rows 0 to 2
```

### **Row label (loc)**

```python
df.loc[0, "name"]
df.loc[:, "age"]    # all rows, age column
```

---

# ✅ **5. Filtering Rows**

```python
df[df["age"] > 20]
df[(df["age"] > 18) & (df["age"] < 30)]
df[df["name"].str.contains("A")]
```

---

# ✅ **6. Adding / Updating Columns**

```python
df["salary"] = [1000, 2000]
df["age_plus_5"] = df["age"] + 5
```

---

# ✅ **7. Removing Columns / Rows**

```python
df.drop("age", axis=1, inplace=True)    # drop column
df.drop(0, axis=0, inplace=True)        # drop row
```

---

# ✅ **8. Sorting**

```python
df.sort_values("age")
df.sort_values("age", ascending=False)
```

---

# ✅ **9. Handling Missing Data**

```python
df.dropna()               # remove missing rows
df.fillna(0)              # replace with 0
df.fillna(df.mean())      # replace with mean
```

---

# ✅ **10. Grouping**

```python
df.groupby("department")["salary"].mean()
df.groupby("city").size()
```

---

# ✅ **11. Merging / Joining**

```python
pd.merge(df1, df2, on="id")
df1.join(df2.set_index("id"), on="id")
```

---

# ✅ **12. Pivot Table**

```python
df.pivot_table(values="salary", index="city", aggfunc="mean")
```

---

# ✅ **13. Date Operations**

```python
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
```

---

# 🟦 Want a PDF version of Pandas Cheat Sheet?

I can generate a **one-page PDF** for printing and sharing.
