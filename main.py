import io
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse

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


# Define a route to stream music
@app.get("/music")
async def get_music():
    # Music by <a href="https://pixabay.com/users/lofium-30660321/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=123560">Lofium</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=123560">Pixabay</a>
    # Open the music file
    with open("lofi-relax-travel-by-lofium-123560.mp3", "rb") as f:
        # Stream the music file using StreamingResponse
        return StreamingResponse(io.BytesIO(f.read()), media_type="audio/mpeg")


@app.get("/lofi")
async def get_video():
    # Video by <a href="https://pixabay.com/users/fifi-tv-30452399/?utm_source=link-attribution&utm_medium=referral&utm_campaign=video&utm_content=201158">Fatima Zahra El ouariaghli</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=video&utm_content=201158">Pixabay</a>
    # Open the video file
    with open("Lofi.mp4", "rb") as f:
        # Stream the video file using StreamingResponse
        return StreamingResponse(
            io.BytesIO(f.read()),
            media_type="video/mp4",
            headers={"Content-Disposition": "inline; filename=Lofi.mp4"},
        )

    # # Open the video file
    # with open("Lofi.mp4", "rb") as f:
    #     # Stream the video file using StreamingResponse
    #     return StreamingResponse(
    #         io.BytesIO(f.read()),
    #         media_type="video/mp4",
    #         headers={"Content-Disposition": "inline; filename=Lofi.mp4"},
    #         status_code=206,  # Enable range requests
    #     )
