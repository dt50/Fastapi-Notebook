from fastapi import FastAPI, HTTPException

from app.api.routes.api import router as api_router
from app.core.events import create_start_app_handler, create_stop_app_handler
from app.api.errors.http_error import http_error_handler


def get_application():
    application = FastAPI(title='FastAPI')
    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))
    application.include_router(api_router, prefix='/api')
    application.add_exception_handler(HTTPException, http_error_handler)
    return application


app = get_application()
