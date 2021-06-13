from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

import uvicorn
from routers import department, object
import models
from models.database import engine
import create_database as db_creator

models.database.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Virtual Microscope API",
              description="API for thesis by student Andrey Otroshchenko",
              docs_url="/docs", redoc_url=None)

app.include_router(department.router, prefix="/departments", tags=["departments"])
app.include_router(object.router, prefix="/objects", tags=["objects"])


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    print(_, exc)
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc}),
    )

if __name__ == '__main__':
    db_creator.create_database(False)

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
