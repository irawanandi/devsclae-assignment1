from app.router.group_test import group_router
from app.router.metode_test import metode_test_router
from app.core.settings import settings
from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)


@app.get(path="/")
def home():
    return {"message": "Devscale Assignment 1 - Fastapi, Alembic, and SQLModel"}


@app.get(path="/scalar-docs")
def scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title=app.title)


app.include_router(metode_test_router)
app.include_router(group_router)
