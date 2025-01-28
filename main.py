from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from core.customs.simple_exceptions import SimpleException
from app.routes import api_routers
from app.db.database_session import sessionmanager
import app.db.sql_base_class

@asynccontextmanager
async def lifespan(app: FastAPI):
    # await init_db()
    yield
    if sessionmanager._engine is not None:
        await sessionmanager.close()


app = FastAPI(title="Simple POS API", lifespan=lifespan)

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
