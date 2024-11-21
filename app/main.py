from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from app.models import InvalidResponse, NationalId, NationalIdData, ValidResponse
from utils.national_id_data import extract_birth_date, extract_birth_date_serial, extract_birth_governerate, extract_gender


app = FastAPI(title="Vaidate National Id Number", version="1.0", debug=True)

@app.post("/validate-nid")
def validate_national_id(request: NationalId):
    nid = request.national_id
    if(len(nid) != 14):
        return InvalidResponse(message="National ID number should be 14 digits")
    try:
        birth_date = extract_birth_date(nid)
        birth_governerate = extract_birth_governerate(nid)
        birth_date_serial = extract_birth_date_serial(nid)
        gender = extract_gender(nid)
    except ValueError as e:
        return InvalidResponse(message=str(e))
    
    return ValidResponse(
            data=NationalIdData(
                    birth_date=birth_date,
                    birth_governerate=birth_governerate,
                    birth_date_serial=birth_date_serial,
                    gender=gender
                )
            )


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return RedirectResponse(url="/docs")