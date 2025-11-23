from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from services.task_service import (
    stats_summary,
    fetch_all_tasks,
    fetch_pending_tasks
)
from ml_model.predict import predict_delay

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/analytics", response_class=HTMLResponse)
def analytics(request: Request):

    stats = stats_summary()
    all_tasks = fetch_all_tasks()
    pending_tasks = fetch_pending_tasks()

    # ---- Priority Distribution ----
    priority_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for t in pending_tasks:
        priority_count[t.priority] += 1

    # ---- ML Predictions for ALL pending tasks ----
    ml_results = []
    for t in pending_tasks:
        pred = predict_delay(t.priority, t.est_days)
        ml_results.append({
            "id": t.id,
            "title": t.title,
            "priority": t.priority,
            "est_days": t.est_days,
            "prediction": pred
        })

    context = {
        "request": request,
        "stats": stats,
        "priority_count": priority_count,
        "ml_results": ml_results,
        "pending_tasks": pending_tasks
    }

    return templates.TemplateResponse("analytics.html", context)
