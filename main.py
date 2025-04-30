from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Optional: serve index.html directly (for now)
@app.get("/", response_class=HTMLResponse)
def read_form():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

# POST handler for form
@app.post("/generate-portraits")
async def generate_portraits(
    gender: str = Form(...),
    face_shape: str = Form(...)
    # Add more fields here
):
    return {
        "status": "success",
        "data": {
            "gender": gender,
            "face_shape": face_shape,
            # add more return fields as needed
        }
    }
