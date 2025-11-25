# project

TOPIC: student record management system.

- a cli application
- store data in json
- keep it modular code.

## what is JSON

- JSON - javascript object notation
- In python terms, JSON is nothing but,
  - dictionary format data is being store.
  - key value pairs are stored.
  - You may store nested dictionary also.
  - it supports string, int, float, list data types.
  - always key suppose to enclosed with double quotes.
  - It is one of the way to store data.

example

```json
[
  {
    "id": 100,
    "name": "sin chan",
    "age": 5
  },
  {
    "id": 101,
    "name": "Jackie chan",
    "age": 78
  }
]
```

## How to access and save dictionary to JSON in python

- in project folder refer `utils/file_handler.py` file.
- Where you can see 2 functions
  - `load_data()` function which get JSON and converts to list of dictionary.
  - `save_data()` function which save list of dictionary to JSON.

## why to keep empty `__init__.py` file in folders

- In our project `utils` and `services` folder has `__init__.py` file. 
- To make python, treat folders as package, we need to add this file in the folder.
- Then only import statement will work. 
- eg: in `app.py` we have this import statement given below. 

```python
from services.student_service import (
    add_student,
    get_all_students,
    get_student,
    update_student,
    delete_student,
)
```

## DOWNLOAD PROJECT zip folder below

click <a  download href="./project.zip"> here </a> to download your project zip file. 
