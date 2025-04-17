from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from user_service.app.exception_handlers import UserBaseException


from user_service.app.routes.user.v1.routes import router as user_router
from user_service.app.routes.auth.v1.auth import router as auth_router
from user_service.app.routes.rental.v1.rent import router as rent_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(user_router, prefix="/api/v1/users")
app.include_router(auth_router)
app.include_router(rent_router, prefix="/api/v1/rents")

@app.exception_handler(HTTPException)
async def http_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status_code":  exc.status_code,
            "message" : "failed",
            "error": exc.detail,
        }
    )

@app.exception_handler(UserBaseException)
async def integrity_error_handler(request: Request, exc : UserBaseException):
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
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")