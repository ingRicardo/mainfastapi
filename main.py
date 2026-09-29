# main.py
from fastapi import FastAPI

# Initialize the FastAPI application instance
app = FastAPI()

# Define a GET route at the root URL ("/")
@app.get("/")
def read_root():
    # FastAPI automatically handles converting dictionaries to JSON responses
    return {"message": "Hello, FastAPI!"}

# Define an optional route with a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query_param": q}
