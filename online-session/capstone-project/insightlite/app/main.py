from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import init_db
from routers import tasks, analytics
import uvicorn


app = FastAPI(title='InsightLite')


# initialize DB
init_db()


# mount static
app.mount('/static', StaticFiles(directory='static'), name='static')


# include routers
app.include_router(tasks.router)
app.include_router(analytics.router)

if __name__ == '__main__':
    uvicorn.run('app.main:app', host='127.0.0.1', port=8000, reload=True)