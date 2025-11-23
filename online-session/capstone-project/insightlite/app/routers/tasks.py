from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from services.task_service import fetch_all_tasks, fetch_task, create_task, update_task, delete_task
from ml_model.predict import predict_delay
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    tasks = fetch_all_tasks()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@router.get("/add", response_class=HTMLResponse)
def add_task_form(request: Request):
    return templates.TemplateResponse("add_task.html", {"request": request})

@router.post("/add")
def add_task(request: Request, title: str = Form(...), description: str = Form(''), priority: int = Form(1), est_days: int = Form(1), due_date: str = Form(None)):
    data = {
        "title": title, 
        "description": description, 
        "priority": priority, 
        "est_days": est_days, 
        "due_date": due_date
    }
    # simple ML prediction (use default historic rate 0.7)
    ml = predict_delay(priority, est_days, 0.7)
    task_id = create_task(data)
    # redirect to home
    return RedirectResponse(url='/', status_code=303)

@router.get("/complete/{task_id}")
def complete_task(task_id: int):
    task = fetch_task(task_id)
    if not task:
        return RedirectResponse('/', status_code=303)
    task['completed'] = 1
    update_task(task_id, task)
    return RedirectResponse(url='/', status_code=303)

@router.get("/delete/{task_id}")
def delete(task_id: int):
    delete_task(task_id)
    return RedirectResponse(url='/', status_code=303)