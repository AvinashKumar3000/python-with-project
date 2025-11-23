# routings

## requirements

install package

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

run server

```bash
uvicorn main:app --reload
```

## http methods

    @app.get()
    @app.post()
    @app.put()
    @app.delete()
    @app.patch()

## when to use

     GET   : get an information
     POST  : insert new data
     PUT   : updating existing data
     DELETE: remove a existing data
     PATCH : any fix

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def getData():
    return { "message": "get method" }

@app.post("/api")
def postData():
    return { "message": "post method" }

@app.put("/api")
def putData():
    return { "message": "put method" }

@app.delete("/api")
def deleteData():
    return { "message": "delete method" }

@app.patch("/api")
def patchData():
    return { "message": "patch method" }
```
