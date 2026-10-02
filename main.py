# main.py
from fastapi import FastAPI
import uvicorn
from controllers.item_controller import router as item_router
from controllers.tuto_controller import router as tuto_router
from controllers.tuto_keywords import router as tuto_keywords
from controllers.tuto_controller_3 import router as tuto_3
from controllers.play_game_controller import router as playgame
from controllers.tuto_controller_4 import router as tuto4

# Initialize the FastAPI application instance
app = FastAPI(title="My FastAPI App")


# Include your controller router into the application instance
app.include_router(item_router)
app.include_router(tuto_router)
app.include_router(tuto_keywords)
app.include_router(tuto_3)
app.include_router(playgame)
app.include_router(tuto4)

# Define a GET route at the root URL ("/")
@app.get("/")
def read_root():
    # FastAPI automatically handles converting dictionaries to JSON responses
    return {"message": "Hello, FastAPI!"}


@app.get("/tutorial")
def tuto():
    print('tutorial')
    return {"message ": "this is a basic tutorial"}

def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()