import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/resume")
async def get_resume():
    json_file_path = os.path.join(os.path.dirname(__file__), "vite-frontend/public/my_info.json")

    # Check if the file exists
    if not os.path.exists(json_file_path):
        return {"error": "JSON file not found"}

    # Read the JSON file
    with open(json_file_path, "r") as file:
        json_data = file.read()

    return {"json_data": json_data}
