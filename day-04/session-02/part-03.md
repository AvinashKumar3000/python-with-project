# matplot lib

Here is a **clean, beginner-friendly Matplotlib Cheat Sheet** — perfect for quick revision and teaching students.

---

# 🎨 **Matplotlib Cheat Sheet (Python)**

---

# ✅ **1. Importing**

```python
import matplotlib.pyplot as plt
```

---

# ✅ **2. Basic Plot**

```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

---

# ✅ **3. Labels & Title**

```python
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("My Graph")
```

---

# ✅ **4. Line Styles**

```python
plt.plot(x, y, linestyle="--")   # dashed  
plt.plot(x, y, linestyle="-")    # solid  
plt.plot(x, y, linestyle=":")    # dotted  
```

---

# ✅ **5. Markers**

```python
plt.plot(x, y, marker="o")      # circle
plt.plot(x, y, marker="s")      # square
plt.plot(x, y, marker="*")      # star
```

---

# ✅ **6. Bar Chart**

```python
plt.bar(categories, values)
plt.show()
```

---

# ✅ **7. Horizontal Bar Chart**

```python
plt.barh(categories, values)
```

---

# ✅ **8. Scatter Plot**

```python
plt.scatter(x, y)
```

---

# ✅ **9. Histogram**

```python
plt.hist(data, bins=5)
```

---

# ✅ **10. Pie Chart**

```python
plt.pie(values, labels=labels, autopct="%1.1f%%")
```

---

# ✅ **11. Multiple Plots in One Figure**

```python
plt.plot(x, y1)
plt.plot(x, y2)
```

---

# ✅ **12. Subplots**

```python
plt.subplot(1, 2, 1)
plt.plot(x, y)

plt.subplot(1, 2, 2)
plt.bar(x, y)

plt.show()
```

---

# ✅ **13. Grid**

```python
plt.grid(True)
```

---

# ✅ **14. Figure Size**

```python
plt.figure(figsize=(6, 4))
```

---

# ✅ **15. Save Plot**

```python
plt.savefig("chart.png")
```

---

# 🟦 Want a **Matplotlib Cheat Sheet PDF**?

I can generate a **one-page PDF version** for printing.
