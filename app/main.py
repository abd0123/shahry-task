from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from app.models import NationalId


app = FastAPI(title="Vaidate National Id Number", version="1.0")

@app.get("/validate-nid")
def validate_national_id(national_id: NationalId):
    return True


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return RedirectResponse(url="/docs")