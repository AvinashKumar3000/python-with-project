# others 

## response body

```python
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    return item
```

- here Item is a class
- which is created by inheriting `BaseModel` from `pydantic`.

## cors

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
