# project

TOPIC: Expense tracker using file operations.

- a cli application
- store data in csv
- keep it modular code.

## what is CSV

- CSV - comma separated value.
- We know excel sheet, which stores data in rows and columns.
- As simple way to keep data in row & cols is csv.
- Each line represents row.
- Each data separated with comma is column values.

example

```csv
id,name,age
12,sample,23
13,Ravi,20
14,Anita,22
15,Karan,24
```

## why to keep empty `__init__.py` file in folders

- In our project `utils` and `services` folder has **init**.py file.
- To make python, treat folders as package, we need to add this file in the folder.
- Then only import statement will work.
- eg: in `app.py` we have this import statement.

## how to read and write csv file.

- Function named `write_row()` in `file_service.py` you can see code for write csv.
- Function named `read_all()` in `file_service.py` you can see code for read csv.

## DOWNLOAD PROJECT zip folder below

click <a  download href="./project.zip"> here </a> to download your project zip file.
