# webscraping
Here is a **clean, simple, exam-friendly Web Scraping Cheat Sheet for Python** — perfect for fast revision.

---

# 🌐 **Python Web Scraping Cheat Sheet**

---

# ✅ **1. Install Required Libraries**

```bash
pip install requests
pip install beautifulsoup4
```

---

# ✅ **2. Import Libraries**

```python
import requests
from bs4 import BeautifulSoup
```

---

# 🚀 **3. Fetch a Webpage**

```python
url = "https://example.com"
response = requests.get(url)

html = response.text   # page source
```

---

# 🥣 **4. Parse HTML using BeautifulSoup**

```python
soup = BeautifulSoup(html, "html.parser")
```

---

# 🔍 **5. Finding Elements**

### **Find first match**

```python
title = soup.find("h1")
```

### **Find all matches**

```python
links = soup.find_all("a")
```

### **Find by class**

```python
items = soup.find_all("div", class_="product")
```

### **Find by id**

```python
box = soup.find(id="main")
```

---

# 🔗 **6. Extracting Text & Attributes**

### **Get text**

```python
title_text = title.get_text()
```

### **Get attribute (href, src, etc.)**

```python
link = soup.find("a")["href"]
```

---

# 📄 **7. Extract All Links**

```python
all_links = [a["href"] for a in soup.find_all("a", href=True)]
```

---

# 📷 **8. Extract All Images**

```python
images = [img["src"] for img in soup.find_all("img")]
```

---

# 🧹 **9. Cleaning Extracted Data**

```python
text = title.get_text(strip=True)
```

---

# 🔄 **10. Loop Through Products Example**

```python
products = soup.find_all("div", class_="product")

for p in products:
    name = p.find("h2").get_text(strip=True)
    price = p.find("span", class_="price").get_text(strip=True)
    print(name, price)
```

---

# 🧾 **11. Save Scraped Data to CSV**

```python
import csv

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Price"])
    writer.writerows(data)
```

---

# ⚠️ **12. Always Check robots.txt**

Example:

```
https://example.com/robots.txt
```

---

# 🚫 **13. Don't Spam Requests**

```python
import time
time.sleep(1)  # wait 1 sec between requests
```

---

# 🛠️ **14. Handle Errors**

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except Exception as e:
    print("Error:", e)
```

---

# ⭐ **15. Useful Tips**

✔ Use browser “Inspect Element” to find tags
✔ Use `.strip()` to clean text
✔ Use `soup.select("css-selector")` for CSS-style querying
✔ Some websites block scraping → use headers or proxies
