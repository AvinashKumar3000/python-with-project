# routing

## path parameters

Path parameters are part of the URL path itself.
They are used to access a specific resource using an identifier like id, name, etc.

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

example routes

- `http://localhost:8000/items/2` 200 OK
- `http://localhost:8000/items/22` 200 OK
- `http://localhost:8000/items/33` 200 OK
- `http://localhost:8000/items/abc` 422 Unprocessable Entity

        NOTE: here the path is changing dynamically
        and single logic / func is able to respond.

## Query Parameters:

Query parameters are passed after the ? symbol in the URL.
They are mainly used for searching, filtering, sorting, or pagination.

```python
@app.get("/search/")
def search_item(q: str = None, limit: int = 10):
    return {"query": q, "limit": limit}
```

example routes

- `http://localhost:8000/search/?q=vanilla`
- `http://localhost:8000/search/?q=chocolate&limit=5`
- `http://localhost:8000/search/` → uses default limit = 10

NOTES:

- q and limit are query parameters.
- They are optional because default values are provided.
- You can pass one or both parameters in any order.

## REQUEST PAYLOAD

- Request payload refers to the data sent by the client (frontend, Postman, or other API client) to the server inside the body of an HTTP request.
- Commonly used with:
  - POST
  - PUT
  - PATCH
- This data usually represents something we want to create or update on the server.

| Method  | Purpose                | Example                            |
| ------- | ---------------------- | ---------------------------------- |
| `POST`  | Create a new resource  | Create a new ice cream             |
| `PUT`   | Update entire resource | Update all details of an ice cream |
| `PATCH` | Update partial data    | Update only price or name          |

## example json payload

```json
{
  "id": 1,
  "name": "Vanilla",
  "category": "Cream",
  "price": 50
}
```

## code example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 01) Define model (structure of expected data)
class IceCream(BaseModel):
    id: int
    name: str
    category: str
    price: float

# 02) Create a POST endpoint to receive payload
@app.post("/ice-creams/")
def create_ice_cream(icecream: IceCream    ):
    # TODO
    return {
        "message": "New ice cream added successfully!",
        "data_received": icecream
    }
```

## Notes:

- Pydantic models automatically validate data types.
- If you send `"price": "abc"`, FastAPI will return a 422 Validation Error.
- Payload can be:
  - JSON (application/json) → Most common
  - Form data (application/x-www-form-urlencoded)
  - Multipart (multipart/form-data) → used when sending files or images
