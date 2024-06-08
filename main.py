import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

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


@app.get("/photo")
async def get_photo(request: Request):
    txt_file_path = os.path.join(os.path.dirname(__file__), "ascii_photo.txt")

    if not os.path.exists(txt_file_path):
        return {"error": "TXT file not found"}

    with open(txt_file_path, "r") as file:
        photo = file.read()

    # Check if the request was made via a browser
    if "text/html" in request.headers.get("accept", ""):
        # If request was made via browser, return ASCII art as HTML
        ascii_art_html = f"<pre>{photo}</pre>"
        return HTMLResponse(content=ascii_art_html)
    else:
        # If request was made programmatically, return ASCII art as plain text
        return photo


    return ascii_art_with_box
