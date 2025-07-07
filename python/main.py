# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from image_generator import generate_image

app = FastAPI()

# Serve the frontend HTML from /static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_homepage():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

class ImageRequest(BaseModel):
    image_url: str
    prompt: str
    negative_prompt: str = ""

@app.post("/generate")
async def generate_image_route(data: ImageRequest):
    try:
        result = generate_image(
            image_url=data.image_url,
            prompt=data.prompt,
            negative_prompt=data.negative_prompt
        )
        return JSONResponse(content={"status": "success", "result": result})
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)})
