

# 🎨 **Tkinter GUI Cheat Sheet (Python)**

---

# ✅ **1. Importing Tkinter**

```python
import tkinter as tk
from tkinter import messagebox
```

---

# ✅ **2. Creating Main Window**

```python
root = tk.Tk()
root.title("My App")
root.geometry("400x300")
root.mainloop()
```

---

# ✅ **3. Basic Widgets**

### **Label**

```python
label = tk.Label(root, text="Hello World")
label.pack()
```

### **Button**

```python
btn = tk.Button(root, text="Click Me", command=my_function)
btn.pack()
```

### **Entry (Input Box)**

```python
entry = tk.Entry(root)
entry.pack()

value = entry.get()       # get text
```

---

# 🚀 **4. Layout Managers**

### **pack()**

Simple vertical/horizontal stacking.

```python
label.pack(side="left")
```

### **grid()**

Table layout.

```python
label.grid(row=0, column=1)
```

### **place()**

Absolute positioning.

```python
label.place(x=50, y=100)
```

---

# ✅ **5. Frame (Container)**

```python
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="OK").pack()
```

---

# 🎨 **6. Styling Widgets**

```python
label = tk.Label(root, text="Name", font=("Arial", 14), bg="yellow", fg="blue")
```

---

# 📌 **7. Message Boxes**

```python
messagebox.showinfo("Title", "Hello")
messagebox.showwarning("Warning", "Be careful!")
messagebox.showerror("Error", "Something went wrong!")
```

---

# 📝 **8. Text Widget**

```python
txt = tk.Text(root, height=5, width=30)
txt.pack()

content = txt.get("1.0", tk.END)
```

---

# 🔄 **9. Listbox**

```python
lb = tk.Listbox(root)
lb.insert(1, "Apple")
lb.insert(2, "Banana")
lb.pack()
```

---

# 📂 **10. File Dialog**

```python
from tkinter import filedialog

file = filedialog.askopenfilename()
```

---

# 🎛️ **11. Checkbutton / Radiobutton**

### **Checkbutton**

```python
var = tk.IntVar()
chk = tk.Checkbutton(root, text="I Agree", variable=var)
chk.pack()
```

### **Radiobutton**

```python
gender = tk.StringVar()

tk.Radiobutton(root, text="Male", value="M", variable=gender).pack()
tk.Radiobutton(root, text="Female", value="F", variable=gender).pack()
```

---

# 📊 **12. Combobox (Dropdown)**

```python
from tkinter.ttk import Combobox

combo = Combobox(root, values=["Python", "Java", "C++"])
combo.pack()
```

---

# 🔘 **13. Menu Bar**

```python
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
```

---

# 🎨 **14. Canvas Drawing**

```python
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

canvas.create_line(0, 0, 200, 100)
canvas.create_rectangle(50, 50, 150, 120, fill="blue")
```

---

# ❤️ **15. Main Loop (must be last)**

```python
root.mainloop()
```
