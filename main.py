from typing import  List
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from domain.health_check import HealthCheck
from service.ui_service import UiService

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse, response_model=HealthCheck)
async def read_root(request: Request):
    data: List[HealthCheck] = UiService.get_most_recent_records()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": [jsonable_encoder(hc) for hc in data] }
    )
