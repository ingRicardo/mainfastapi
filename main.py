# main.py
from fastapi import FastAPI
from controllers.item_controller import router as item_router
from controllers.tuto_controller import router as tuto_router


# Initialize the FastAPI application instance
app = FastAPI(title="My FastAPI App")


# Include your controller router into the application instance
app.include_router(item_router)
app.include_router(tuto_router)

# Define a GET route at the root URL ("/")
@app.get("/")
def read_root():
    # FastAPI automatically handles converting dictionaries to JSON responses
    return {"message": "Hello, FastAPI!"}


@app.get("/tutorial")
def tuto():
    print('tutorial')
    return {"message ": "this is a basic tutorial"}
    