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

@main.get ("/women_3", response_class=HTMLResponse)
async def women_3(request: Request):
    return  templates.TemplateResponse("women_3.html", context={"request": request})

@main.get("/men_1", response_class=HTMLResponse)
async def men_1(request: Request):
    return templates.TemplateResponse("men_1.html", context={"request": request})

@main.get("/men_2", response_class=HTMLResponse)
async def men_2(request: Request):
    return templates.TemplateResponse("men_2.html", context={"request": request})

@main.get("/men_3", response_class=HTMLResponse)
async def men_3(request: Request):
    return templates.TemplateResponse("men_3.html", context={"request": request})

@main.get("/about_us", response_class=HTMLResponse)
async def about_us(request: Request):
    return templates.TemplateResponse("about_us.html", context={"request": request})

@main.get("/our_projects", response_class=HTMLResponse)
async def our_projects_1(request: Request):
    return templates.TemplateResponse("our_projects.html", context={"request": request})

@main.get("/our_projects_2", response_class=HTMLResponse)
async def our_projects_2(request: Request):
    return templates.TemplateResponse("our_projects_2.html", context={"request": request})
@main.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    return templates.TemplateResponse("services.html", context={"request": request})

@main.get("/log_account", response_class=HTMLResponse)
async def log_account(request: Request):
    return templates.TemplateResponse("log_account.html", context={"request": request})

@main.get("/registr_page", response_class=HTMLResponse)
async def registr_page(request: Request):
    return templates.TemplateResponse("registr_page.html", context={"request": request})

@main.get("/profil", response_class=HTMLResponse)
async def profil(request: Request):
    return templates.TemplateResponse("profil.html", context={"request": request})