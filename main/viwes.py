#будут пути к html

from pydantic import BaseModel
import time
from main import main, templates, g
from fastapi import Request, status
from fastapi.exceptions import ValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
#from main.models.database import

@main.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("main.html", context={"request": request, "TEST":"hekjfa"})

@main.get("/women_1", response_class=HTMLResponse)
async def women_katalog(request: Request):
    return templates.TemplateResponse("women_1.html", context={"request": request})

@main.get("/women_2", response_class=HTMLResponse)
async def women_2(request: Request):
    return templates.TemplateResponse("women_2.html", context={"request": request})

# @main.get("/", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("services.html", context={"request": request})
