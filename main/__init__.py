from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

main = FastAPI(title="CHERNIKOY-STORE")
main.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class g:
    db = None
    current_user = None

from main import viwes


