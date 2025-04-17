from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from book_service.app.exception_handlers import BookBaseException
from book_service.app.routes.v1.routes import router as book_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(book_router, prefix="/api/v1/books")

@app.exception_handler(HTTPException)
async def http_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status_code":  exc.status_code,
            "message" : "failed",
            "error": exc.detail
        }
    )

@app.exception_handler(BookBaseException)
async def integrity_error_handler(request: Request, exc : BookBaseException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message" : "failed",
            "error" : str(exc)
        }
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={
            "status_code" : 400,
            "messages" : "failed",
            "error": str(exc.errors())
        }
        )



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")