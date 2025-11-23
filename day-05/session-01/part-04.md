

# 🚀 **Automation Scripts Cheat Sheet (os, shutil, smtplib)**

---

## 🗂 **1. `os` Module — File & Directory Automation**

### 🔹 **Basics**

```python
import os
```

### 📁 **Working with Directories**

```python
os.getcwd()               # Get current working directory
os.chdir("path")          # Change directory
os.listdir("path")        # List items in directory
os.mkdir("new_folder")    # Create a directory
os.makedirs("a/b/c")      # Create nested directories
os.rmdir("folder")        # Remove empty directory
os.removedirs("a/b/c")    # Remove nested directories (empty only)
```

### 📄 **Working with Files**

```python
os.remove("file.txt")             # Delete file
os.rename("old.txt", "new.txt")   # Rename file or folder
os.path.exists("path")            # Check if file/folder exists
```

### 🛣 **Path Handling**

```python
os.path.join("folder", "file.txt")  
os.path.abspath("file.txt")        
os.path.basename("/path/file.txt") 
os.path.dirname("/path/file.txt")
```

---

## 📦 **2. `shutil` Module — High-Level File Operations**

### 🔹 **Basics**

```python
import shutil
```

### 📁 **Copy Files**

```python
shutil.copy("src.txt", "dest/")         # Copy file → keeps filename
shutil.copy2("src.txt", "dest/")        # Copy with metadata
```

### 📂 **Copy Entire Folder**

```python
shutil.copytree("src_folder", "new_folder")
```

### ❌ **Delete Files/Folders**

```python
shutil.rmtree("folder")   # Remove directory with content
```

### 🚚 **Move Files**

```python
shutil.move("file.txt", "destination_folder/")
```

### 💾 **Archive (Zip)**

```python
shutil.make_archive("backup", "zip", "folder_to_zip")
```

---

## ✉️ **3. `smtplib` — Automate Email Sending**

### 🔹 **Basics**

```python
import smtplib
from email.message import EmailMessage
```

### 📧 **Send Simple Email (Gmail Example)**

```python
email = EmailMessage()
email["From"] = "you@gmail.com"
email["To"] = "receiver@gmail.com"
email["Subject"] = "Automated Report"
email.set_content("Hi, this is an automated email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("you@gmail.com", "your_app_password")
    smtp.send_message(email)
```

✔️ **Note:**
Gmail requires an *App Password* (not your usual password).

---

## 📎 **Send Email With Attachments**

```python
email = EmailMessage()
email["From"] = "you@gmail.com"
email["To"] = "receiver@gmail.com"
email["Subject"] = "Report"
email.set_content("Please find the attachment.")

# Attach file
with open("report.pdf", "rb") as f:
    email.add_attachment(f.read(), 
                         maintype="application", 
                         subtype="pdf", 
                         filename="report.pdf")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("you@gmail.com", "your_app_password")
    smtp.send_message(email)
```

---

# 🧠 Summary Table

| Task                | Module  | Function                   |
| ------------------- | ------- | -------------------------- |
| Create/Delete files | os      | remove(), rmdir(), mkdir() |
| Copy file           | shutil  | copy(), copy2()            |
| Move file           | shutil  | move()                     |
| Create archive      | shutil  | make_archive()             |
| Send email          | smtplib | SMTP_SSL(), send_message() |

