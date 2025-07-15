from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from core.font_generator import generate_font

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-font")
async def handle_generate_font(request: Request):
    data = await request.json()
    keywords = data.get('keywords', [])

    if not keywords:
        return JSONResponse(content={'error': 'Keywords are required'}, status_code=400)

    # Here we call our font generation logic.
    font_path = generate_font(keywords)

    return JSONResponse(content={'font_path': font_path})
