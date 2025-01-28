from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from core.customs.simple_exceptions import SimpleException
import app.db.sql_base_class
from app.routes import api_routers

app = FastAPI(title="Simple POS API")


app.include_router(api_routers)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.exception_handler(SimpleException)
async def simple_exception_handler(request: Request, exception: SimpleException):
    if isinstance(exception, SimpleException):
        response_dict = {
            "message": exception.message,
            "type": exception.err_type.value,
        }

        return JSONResponse(
            status_code=exception.status_code,
            content=response_dict,
        )
