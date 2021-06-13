from fastapi import FastAPI

import uvicorn
from routers import department, object
import models
from models.database import engine

models.database.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Virtual Microscope API",
              description="API for thesis by student Andrey Otroshchenko",
              docs_url="/docs", redoc_url=None)


app.include_router(department.router, prefix="/departments", tags=["departments"])
app.include_router(object.router, prefix="/objects", tags=["objects"])

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
