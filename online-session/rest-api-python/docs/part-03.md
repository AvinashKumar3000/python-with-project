# scenario

## status code

    Use Case	        Status Code
    GET  Success	    200 OK
    POST Success        (New Resource)	201 Created
    PUT/PATCH Success	200 OK or 204 No Content
    DELETE Success	    204 No Content
    Invalid Input	    400 Bad Request
    Unauthorized        (Invalid Token)	401 Unauthorized
    Access Denied       (Role Issue)	403 Forbidden
    Not Found	        404 Not Found
    Duplicate Record	409 Conflict
    Validation Failed	422 Unprocessable Entity
    Internal Error	    500 Internal Server Error

## questions

you have an ice-cream company.
the company name is `arun-icecream`.
Where you have a REST-API service.
which will response to the request.

    GET all         : get all icream details
    GET id          : get icream details by id
    GET category    : get by category

```python

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Arun Icecream API", version="1.0")

ice_creams = [
    {"id": 1, "name": "Vanilla Cup", "category": "cup", "price": 25},
    {"id": 2, "name": "Chocolate Cone", "category": "cone", "price": 30},
    {"id": 3, "name": "Strawberry Stick", "category": "stick", "price": 20},
    {"id": 4, "name": "ButterScotch Cup", "category": "cup", "price": 28},
    {"id": 5, "name": "Mango Cone", "category": "cone", "price": 32},
]

@app.get("/ice_creams")
def get_all_ice_creams():
    return {
        "company": "Arun Ice cream", 
        "count":    len(ice_creams), "data": ice_creams
    }

@app.get("/ice_creams/{ice_cream_id}")
def get_ice_cream_by_id(ice_cream_id: int):
    for ice_cream in ice_creams:
        if ice_cream["id"] == ice_cream_id:
            return {
                "company": "Arun Ice cream", 
                "data": ice_cream
            }
    raise HTTPException(status_code=404, detail="Ice cream not found")

@app.get("/ice_creams/category/{category_name}")
def get_icecream_by_category(category_name: str):
    category_items = [i for i in ice_creams if i["category"].lower() == category_name.lower()]
    
    if not category_items:
        raise HTTPException(status_code=404, detail=f"No ice_creams found in '{category_name}' category.")
    
    return {
        "company": "Arun Icecream", 
        "category": category_name, 
        "count": len(category_items), 
        "data": category_items
    }
```
